from django import forms
from .models import Profile

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField(label='Email')
    # birth_date = forms.DateField(label='Birth date', widget=forms.DateInput(attrs={'type': 'date'}))


class UpdateUserForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)


# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)

    # class Meta:
    #     model = User
    #     fields = ['username', 'first_name', 'last_name', 'email']
