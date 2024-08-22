# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
