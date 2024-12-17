import pytest
from unittest.mock import patch, MagicMock
from app.email_service import send_email_with_sendgrid
from app.email_service import SENDGRID_API_KEY

class MockResponse:
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body

    def json(self):
        return {"status": self.status_code, "body": self.body}

@patch("app.email_service.SendGridAPIClient")  
def test_send_email_with_sendgrid(mock_sendgrid_client):
    mock_client = MagicMock()
    mock_sendgrid_client.return_value = mock_client

    mock_from_email = MagicMock()
    mock_from_email.email = "vhoang@hilltopmfi.org"
    
    mock_client.send.return_value = MockResponse(202, "Email sent successfully")
    
    send_email_with_sendgrid("test@example.com", "Test Subject", "<p>Test Email Content</p>")

    mock_client.send.assert_called_once()
    args, kwargs = mock_client.send.call_args
    message = args[0]

    assert message.from_email is not None
    assert message.from_email.email == "vhoang@hilltopmfi.org"





