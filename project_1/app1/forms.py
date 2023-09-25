from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Reg_form(forms.Form):
    father = forms.CharField(max_length=100)
    mother = forms.CharField(max_length=100)
    age = forms.IntegerField(max_value=100)
    mobile = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea)
    

class log_In(forms.Form):
    
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class signup_form(UserCreationForm):
    email = forms.EmailField
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        
    def __init__(self, *args: Any, **kwargs):
        super(signup_form,self).__init__(*args, **kwargs)
        self.fields['username'].help_text=""
        self.fields['password1'].help_text=""
        self.fields['password2'].help_text=""

    # username = forms.CharField(max_length=100)
  
    # email=forms.EmailField(max_length=100)
    # password = forms.CharField(widget=forms.PasswordInput)
    # re_password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     pass1=self.cleaned_data['password']
    #     pass2 = self.cleaned_data['re_password']
    #     if pass1 != pass2:
    #         return ValidationError('Passwords does not match')

class forgot_pass(forms.Form):
    username = forms.CharField(max_length=100)
    old_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = forms.CharField(max_length=100) 
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['re_password']
        if pass1 != pass2:
            return ValidationError('Passwords does not match')


