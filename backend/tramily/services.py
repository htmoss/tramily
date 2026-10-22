import os
import resend
import secrets
import hashlib
from resend.exceptions import ResendError
from tramily.models import User

resend.api_key = os.environ["RESEND_API_KEY"]
test_email = os.environ["TEST_EMAIL"]

def check_existing_user(email: str):
    return User.objects.filter(email=email).exists()

def create_link():
    token = secrets.token_urlsafe()
    hashed_token = hashlib.sha256(token.encode())
    return f"http://localhost:5173/api/auth/verify/?token={hashed_token.hexdigest()}"

def send_email(email: str):
    link = create_link()
    print("link is here:", link)
    params: resend.Emails.SendParams = {
    "from": "Tramily <onboarding@resend.dev>",
    "to": [test_email],
    "subject": "hello, click here to sign into tramily",
    "html": f"<a href={link}><button>Click me</button></a>"
    }
    try:
        email = resend.Emails.send(params)
        print(email)
    except ResendError as error:
        print(error)

def send_new_user_email(email: str):
    params: resend.Emails.SendParams = {
    "from": "Tramily <onboarding@resend.dev>",
    "to": [test_email],
    "subject": "hello, click here to sign up for tramily",
    "html": "<p>it works!</p>"
    }

    try:
        email = resend.Emails.send(params)
        print(email)
    except ResendError as error:
        print(error)

