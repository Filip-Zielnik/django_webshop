from django import forms


class LoginForm(forms.Form):
    pass


class RegistrationForm(forms.Form):
    pass


class UserForm(forms.Form):
    username = forms.CharField(label='login')
    password = forms.CharField(widget=forms.PasswordInput)
