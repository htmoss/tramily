from ninja import NinjaAPI
api = NinjaAPI()

api.add_router('/users/', 'tramily.routers.users.router')
api.add_router('/friendships/', 'tramily.routers.friendships.router')
api.add_router('/auth/', 'tramily.routers.auth.router')

