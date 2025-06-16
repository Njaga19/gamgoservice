from flask import Flask, request, render_template, redirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

EMAIL_ADDRESS = "gamgoservice@gmail.com"
EMAIL_PASSWORD = "bqzftvkvapfdxcqh"
RECEIVER_EMAIL = "gamgoservice@gmail.com"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/become-driver", methods=["POST"])
def become_driver():
    name = request.form["name"]
    license = request.form["license"]
    car_type = request.form["car_type"]
    email = request.form["email"]
    phone = request.form["phone"]

    html_content = f"""    <h2>🚗 New Driver Application</h2>
    <ul>
        <li><strong>Name:</strong> {name}</li>
        <li><strong>License Number:</strong> {license}</li>
        <li><strong>Car Type:</strong> {car_type}</li>
        <li><strong>Email:</strong> {email}</li>
        <li><strong>Phone:</strong> {phone}</li>
    </ul>
    """

    send_html_email("New Driver Application", html_content)
    return render_template("thankyou.html")

@app.route("/request-pickup", methods=["POST"])
def request_pickup():
    name = request.form["name"]
    pickup = request.form["pickup"]
    destination = request.form["destination"]
    phone = request.form["phone"]

    html_content = f"""    <h2>📍 New Pickup Request</h2>
    <ul>
        <li><strong>Name:</strong> {name}</li>
        <li><strong>Pickup Location:</strong> {pickup}</li>
        <li><strong>Destination:</strong> {destination}</li>
        <li><strong>Phone:</strong> {phone}</li>
    </ul>
    """

    send_html_email("New Pickup Request", html_content)
    return render_template("thankyou.html")

def send_html_email(subject, html_body):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = RECEIVER_EMAIL

        part = MIMEText(html_body, "html")
        msg.attach(part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg.as_string())
    except Exception as e:
        print("Email sending failed:", e)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)