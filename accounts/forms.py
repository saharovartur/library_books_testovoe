from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts import models
from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput())
    is_staff = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']






