from django.contrib import admin
from .models import  logIn,login_Register

# Register your models here.
from django.contrib.auth.admin import UserAdmin




admin.site.register(logIn)
admin.site.register(login_Register)

