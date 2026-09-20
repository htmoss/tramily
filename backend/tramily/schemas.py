from ninja import ModelSchema, Schema
from .models import User, TransitLine, Station, UserLocationState, Friendship

class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]

class UserCreateSchema(Schema):
    username: str
    email: str
    first_name: str
    last_name: str

class TransitLineSchema(ModelSchema):
    class Meta:
        model = TransitLine
        fields = ["id", "line_name", "line_color"]

class StationSchema(ModelSchema):
    class Meta:
        model = Station
        fields = ["id", "station_name", "display_order", "latitude", "longitude"]

class UserLocationStateSchema(ModelSchema):
    station: StationSchema | None
    class Meta:
        model = UserLocationState
        fields = ["id", "station", "updated_at"]

class FriendshipSchema(ModelSchema):
    user: UserSchema | None
    friend: UserSchema | None
    class Meta:
        model = Friendship
        fields = ["id", "user", "friend", "status", "created_at"]

class Error(Schema):
    message: str