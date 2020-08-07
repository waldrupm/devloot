from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=150)
    username = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
