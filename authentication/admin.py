from django.contrib import admin
from .models import User, Profile, Address, UserToken, Reset
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(UserToken)
admin.site.register(Reset)
