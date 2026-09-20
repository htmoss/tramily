from ninja import NinjaAPI
from tramily.models import User
from tramily.schemas import UserSchema

api = NinjaAPI()

@api.get('users/', response=list[UserSchema])
def get_users(request):
    return User.objects.all()