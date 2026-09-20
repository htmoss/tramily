from ninja import ModelSchema
from .models import User, TransitLine, Station, UserLocationState, Friendship

class UserSchema(ModelSchema):
    class Config:
        model = User
        model_fields = ["id", "username", "email", "first_name", "last_name"]

class TransitLineSchema(ModelSchema):
    class Config:
        model = TransitLine
        model_fields = ["id", "line_name", "line_color"]

class StationSchema(ModelSchema):
    class Config:
        model = Station
        model_fields = ["id", "station_name", "display_order", "latitude", "longitude"]

class UserLocationStateSchema(ModelSchema):
    station: StationSchema | None
    class Config:
        model = UserLocationState
        model_fields = ["id", "station", "updated_at"]

class FriendshipSchema(ModelSchema):
    user: UserSchema | None
    friend: UserSchema | None
    class Config:
        model = Friendship
        model_fields = ["id", "user", "friend", "status", "created_at"]