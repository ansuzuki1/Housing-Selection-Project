import os

from dotenv import load_dotenv
from gspread_models.service import SpreadsheetService
from gspread_models.base import BaseModel
import gspread
from google.oauth2.service_account import Credentials

load_dotenv()

# google credentials:
DEFAULT_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "google-credentials.json")
GOOGLE_CREDENTIALS_FILEPATH = os.getenv("GOOGLE_CREDENTIALS_FILEPATH", default=DEFAULT_FILEPATH)


# google sheets document:
GOOGLE_SHEETS_DOCUMENT_ID = os.getenv("GOOGLE_SHEETS_DOCUMENT_ID")

# configure the base model to use this info:
service = SpreadsheetService(
    credentials_filepath=GOOGLE_CREDENTIALS_FILEPATH,
    document_id=GOOGLE_SHEETS_DOCUMENT_ID
)
BaseModel.service = service

# now you can import the base model from here, and child model classes will use the configured document
# see: https://pypi.org/project/gspread-models/

SERVICE_ACCOUNT_FILE = GOOGLE_CREDENTIALS_FILEPATH  # Use the same credentials file
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


#Client
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

