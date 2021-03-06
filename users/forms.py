from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    # i will modify email
    email = forms.EmailField(max_length=120, required=True, help_text='Enter  a valid email address')
    class Meta:
        model = User
        fields = ['username','email','password1','password2']