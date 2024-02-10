from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    filter_horizontal = ("groups", "user_permissions")


CustomUserAdmin.fieldsets += ('Custom fields set', {'fields': ('phone_number',)}),

admin.site.register(User, CustomUserAdmin)