from ninja import NinjaAPI
from tramily.models import User
from tramily.schemas import UserSchema
from django.shortcuts import get_object_or_404

api = NinjaAPI()

@api.get('users/', response=list[UserSchema])
def get_users(request):
    return User.objects.all()

@api.get('users/{id}/', response=UserSchema)
def get_user(request, id: int):
    return get_object_or_404(User, id=id)

