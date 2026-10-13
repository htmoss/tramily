import os
import resend
from resend.exceptions import ResendError

resend.api_key = os.environ["RESEND_API_KEY"]

def send_email(email: str):
    params: resend.Emails.SendParams = {
    "from": "Tramily <onboarding@resend.dev>",
    "to": [email],
    "subject": "hello world",
    "html": "<p>it works!</p>"
    }

    try:
        email = resend.Emails.send(params)
        print(email)
    except ResendError as error:
        print(error)


