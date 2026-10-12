from ninja import Router
from tramily.models import User
from tramily.schemas import UserSchema, UserCreateSchema
from django.shortcuts import get_object_or_404

router = Router()

@router.get('/', response=list[UserSchema])
def get_users(request):
    return User.objects.all()

@router.get('/{id}/', response=UserSchema)
def get_user(request, id: int):
    return get_object_or_404(User, id=id)

@router.post('/', response=UserSchema)
def create_user(request, user: UserCreateSchema):
    user_data = user.model_dump()
    user_instance = User.objects.create(**user_data)
    return user_instance