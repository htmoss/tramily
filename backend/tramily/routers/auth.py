from ninja import Router, Status
from email_validator import validate_email, EmailNotValidError


router = Router()

@router.post('/magic-link/')
def send_magic_link(request, email: str):
    # validates that it's an email
    try:
        emailinfo = validate_email(email)
        email_norm = emailinfo.normalized
        # send_email(email_norm)
    except EmailNotValidError as e:
        return str(e)
    return None