from ninja import NinjaAPI
from tramily.models import Friendship, User
from tramily.schemas import FriendshipSchema, UserSchema, UserCreateSchema, Error
from django.shortcuts import get_object_or_404

api = NinjaAPI()

# user routes
@api.get('users/', response=list[UserSchema])
def get_users(request):
    return User.objects.all()

@api.get('users/{id}/', response=UserSchema)
def get_user(request, id: int):
    return get_object_or_404(User, id=id)

@api.post('users/', response=UserSchema)
def create_user(request, user: UserCreateSchema):
    user_data = user.model_dump()
    user_instance = User.objects.create(**user_data)
    return user_instance

# friendship routes
@api.get('friendships/{id}/', response=FriendshipSchema)
def get_friendship(request, id: int):
    return get_object_or_404(Friendship, id=id)


