from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# from .forms import ProfileCreationForm,ProfileChangeForm
from .models import Profile
# Register your models here.
# admin.site.unregister(Profile)
admin.site.register(Profile)
