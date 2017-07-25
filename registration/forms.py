from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Registration(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'reginput'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)
