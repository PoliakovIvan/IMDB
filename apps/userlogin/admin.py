from django.contrib import admin
from apps.userlogin.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

