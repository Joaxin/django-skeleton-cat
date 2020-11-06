from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
