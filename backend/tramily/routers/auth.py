from ninja import Router, Status

router = Router()

@router.post('auth/magic-link')
def send_magic_link(request, email: str):
    # logic here
    return None