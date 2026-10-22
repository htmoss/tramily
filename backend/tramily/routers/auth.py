from ninja import Router, Status
from email_validator import validate_email, EmailNotValidError
from tramily.services import send_email, check_existing_user, send_new_user_email


router = Router()

@router.post('/magic-link/')
def send_magic_link(request, email: str):
    # validates that it's an email
    try:
        emailinfo = validate_email(email)
        email_norm = emailinfo.normalized
        is_existing_user = check_existing_user(email_norm)
        if(is_existing_user):
            send_email(email_norm)
        else:
            send_new_user_email(email_norm)
    except EmailNotValidError as e:
        return str(e)
    return None

@router.post('/verify/')
def verify_magic_link(request, token: str):
    print("token is", token)
    return None