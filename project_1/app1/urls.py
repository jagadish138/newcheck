from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.log_me,name='login'),
    path('register/',views.register,name='register'),
    path("forgot_p/",views.forgot_password,name='password'),
    path("personal/",views.personal,name='personal')
   
]