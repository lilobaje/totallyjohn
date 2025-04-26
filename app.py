from flask import Flask, render_template, request
# Import for sending emails (if you choose to)
# from flask_mail import Mail, Message

app = Flask(__name__)

# --- Optional: Configure Flask-Mail if you want to send emails ---
# app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
# app.config['MAIL_PORT'] = 587  # Or 465 for SSL
# app.config['MAIL_USE_TLS'] = True  # Or False if using SSL
# app.config['MAIL_USERNAME'] = 'your_email_address@example.com'
# app.config['MAIL_PASSWORD'] = 'your_email_password'
# app.config['MAIL_DEFAULT_SENDER'] = 'your_email_address@example.com'

# mail = Mail(app)
# --- End of Flask-Mail Configuration ---

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'name' in request.form and 'email' in request.form and 'message' in request.form:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            # In a real application, you would send this data via email
            print(f"Received contact form submission:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")
            return render_template("index.html", success="Message sent successfully!")
        else:
            return render_template("index.html", error="Please fill out all fields.")
    return render_template("index.html")

# This is the route to handle the contact form submission
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:
            # --- Process the contact form data here ---
            print(f"Received contact form submission:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Message: {message}")

            # --- Optional: Send email using Flask-Mail ---
            # try:
            #     msg = Message("New Contact Form Submission", recipients=['your_recipient_email@example.com'])
            #     msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            #     mail.send(msg)
            #     return render_template("index.html", success="Message sent successfully!")
            # except Exception as e:
            #     print(f"Error sending email: {e}")
            #     return render_template("index.html", error="An error occurred while sending your message. Please try again later.")
            # --- End of Optional Email Sending ---

            # For now, just render the index page with a success message
            return render_template("index.html", success="Message sent successfully!")
        else:
            # If any required field is missing, show an error
            return render_template("index.html", error="Please fill out all fields.")

    # If someone tries to access /submit_contact directly with a GET request,
    # you can redirect them to the homepage or show an error.
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)