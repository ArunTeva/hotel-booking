from dataclasses import field, fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . models import *
class SignUpForm(UserCreationForm):
    class Meta:
        model=CustomeUser
        fields=['email']

class LoginForm(forms.Form):
   
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

    
  

# class ProfileForm(forms.ModelForm):

#     class  Meta:
#         model=CustomeUser
#         fields =['first_name','last_name','profile_image','gender','dob','email','mobile','roll','address','city','state','country',]

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomeUser
        fields = ['first_name','last_name','profile_image','dob','roll','address','city','state','country']
class BookingForm(forms.ModelForm):

    class Meta:
        model=Booking
        fields='__all__'