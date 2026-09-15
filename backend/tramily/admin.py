from django.contrib import admin

from tramily.models import User, TransitLine, Station, UserLocationState, Friendship

# Register your models here.
admin.site.register(User)
admin.site.register(TransitLine)
admin.site.register(Station)
admin.site.register(UserLocationState)
admin.site.register(Friendship)
