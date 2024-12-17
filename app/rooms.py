from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.email_service import SENDGRID_API_KEY
from app.email_service import send_email_with_sendgrid

from app.db import BaseModel

from app.db import client



def fetch_rooms(document_id="10-qQmXxIiJUHPDqQ4Te-btk_yImpR10Pp5x57f4ZaxI", sheet_name="Sheet1"):
    service = BaseModel.service
    doc = client.open_by_key(document_id)
    sheet = doc.worksheet(sheet_name)
    data = sheet.get_all_records()



    rooms = {}
    for n in data:
        room_id = n['room_id']
        status=n['status']
        beds=['beds']
        rooms[room_id]={"beds":n["beds"],"status":n["status"],"view":n["room_view"]}
    return rooms



# Function to fetch and filter rooms based on user input
def fetch_and_filter_rooms(user_filter):
    user_filter = user_filter.lower()

    rooms = fetch_rooms()

    matching_rooms = []
    for room_id, room_details in rooms.items():
        if user_filter == "available":
            if room_details['status'] == "Available":
                matching_rooms.append({room_id: room_details})

        elif user_filter == "1":
            if room_details['beds'] == 1:
                matching_rooms.append({room_id: room_details})

        elif user_filter == "2":
            if room_details['beds'] == 2:
                matching_rooms.append({room_id: room_details})

        elif user_filter == "car barn":
            if room_details['view'] == "Car Barn":
                matching_rooms.append({room_id: room_details})

        elif user_filter == "courtyard":
            if room_details['view'] == "Courtyard":
                matching_rooms.append({room_id: room_details})

        elif user_filter == "lxr":
            if room_details['view'] == "LXR":
                matching_rooms.append({room_id: room_details})

        elif user_filter == "n street":
            if room_details['view'] == "N Street":
                matching_rooms.append({room_id: room_details})

    return matching_rooms

'''
# asking user to input filter keyword:
user_filter = input("Please enter your desired filter: ").lower()
matching_rooms = fetch_and_filter_rooms(user_filter)

# Print matching rooms before sending email
print("\nHere are the rooms matching your filter:\n")
for room in matching_rooms:
    room_id, details = list(room.items())[0]  # Unpack room_id and details
    print(
        f"Room ID: {room_id} | Beds: {details.get('beds', 'N/A')} | "
        f"Status: {details.get('status', 'N/A')} | View: {details.get('view', 'N/A')}"
    )
'''

def generate_email_content(user_filter, matching_rooms):
    emailContent = f"""
    <h1>Your Room List</h1>
    <p>-----------------------------------------</p>
    <p>Here are the rooms matching your search:</p>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <th>Room ID</th>
            <th>Status</th>
            <th>Beds</th>
            <th>View</th>
        </tr>
    """

    for room in matching_rooms:
        room_id, details = list(room.items())[0]  
        emailContent += f"""
        <tr>
            <td>{room_id}</td>
            <td>{details.get('status', 'N/A')}</td>
            <td>{details.get('beds', 'N/A')}</td>
            <td>{details.get('view', 'N/A')}</td>
        </tr>
        """

    emailContent += """
    </table>
    <p>-----------------------------------------</p>
    <p>Thank you for using our service!</p>
    """

    return emailContent

'''emailContent = generate_email_content(user_filter, matching_rooms)

# asking user if they want a list emailed
# --------

sendEmailBool = False

while True:
    sendEmail = input("Do you want a room list sent to your email? (yes or no) ")
    if sendEmail.lower() == "yes":
        customerEmail = input("Please input your email: ")
        sendEmailBool = True
        break
    elif sendEmail.lower() == "no":
        sendEmailBool = False
        print("The email has been sent to your email address!")
        break
    else:
        print("Input invalid, please try again.")

# sending the receipt via email

if sendEmailBool == True:
    send_email_with_sendgrid(recipient_address=customerEmail,
                             subject="Here is your requested room list!",
                             html_content=emailContent)
'''