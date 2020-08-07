from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'shadow border rounded w-full py-2 px-3 text-gray-800 mb-3'})
        self.fields['password2'].widget.attrs.update({'class': 'shadow border rounded w-full py-2 px-3 text-gray-800 mb-3'})

    email = forms.EmailField(max_length=150)
    username = forms.CharField(max_length=30)

    email.widget.attrs.update({'class': 'shadow border rounded w-full py-2 px-3 text-gray-800 mb-2'})
    username.widget.attrs.update({'class': 'shadow border rounded w-full py-2 px-3 text-gray-800 mb-2'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
