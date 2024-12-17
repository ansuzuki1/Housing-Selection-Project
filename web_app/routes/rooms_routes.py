from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.rooms import fetch_and_filter_rooms, generate_email_content
from app.email_service import send_email_with_sendgrid

rooms_routes = Blueprint("rooms_routes", __name__)


@rooms_routes.route("/rooms_form")
def rooms_form():
    return render_template("rooms_form.html")

@rooms_routes.route("/rooms_list", methods=["GET", "POST"])
def rooms_list():
    if request.method == "POST":
        # Handle data sent via POST request (form data)
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # Handle data sent via GET request (URL params)
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)
    
    # Extract the filter value from the form or URL parameters
    filter_value = request_data['filter']
    listofrooms = fetch_and_filter_rooms(filter_value)

    # Check if the user wants to email the results
    send_email_bool = request_data.get('send_email', False)

    if send_email_bool:
        # Generate the email content
        email_content = generate_email_content(filter_value, listofrooms)
        
        # Extract the recipient email address (assuming it's provided via form)
        customer_email = request_data.get('email', '')
        
        if customer_email:
            # Send the email with the generated content
            send_email_with_sendgrid(recipient_address=customer_email,
                                     subject="Here is your requested room list!",
                                     html_content=email_content)
            flash("Email sent successfully!", "success")
        

        else:
            flash("Please provide a valid email address.", "error")
    
    return render_template("rooms.html", listofrooms=listofrooms)




