from ninja import Router
from tramily.models import Friendship
from tramily.schemas import FriendshipSchema
from django.shortcuts import get_object_or_404

router = Router()

@router.get('/{id}/', response=FriendshipSchema)
def get_friendship(request, id: int):
    return get_object_or_404(Friendship, id=id)