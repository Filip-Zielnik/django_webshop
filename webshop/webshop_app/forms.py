from django import forms
from .models import Profile

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Imię', required=False)
    last_name = forms.CharField(label='Nazwisko', required=False)
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(label='Data urodzin', widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Profile
        fields = ('birth_date', )


class UpdateUserForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, label='Imię')
    last_name = forms.CharField(max_length=100, required=False, label='Nazwisko')


# class UpdateUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)

    # class Meta:
    #     model = User
    #     fields = ['username', 'first_name', 'last_name', 'email']
