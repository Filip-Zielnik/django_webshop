from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Profile, Address

from django.contrib.auth.models import User


class FormCleanMixin(ModelForm):
    def clean(self):
        super(FormCleanMixin, self).clean()
        birth_date = self.cleaned_data.get('birth_date')
        user_age = (date.today() - birth_date).days / 365
        if user_age < 18:
            self._errors['birth_date'] = self.error_class(
                ['Musisz mieć co najmniej 18 lat żeby się zarejestrować!']
            )
        return self.cleaned_data


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


class ProfileForm(FormCleanMixin):
    birth_date = forms.DateField(
        label='Data urodzin',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )

    class Meta:
        model = Profile
        fields = ('birth_date',)


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='Nazwa użytkownika')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {'username': 'Nazwa użytkownika',
                  'first_name': 'Imię',
                  'last_name': 'Nazwisko',
                  'email': 'Email',
                  }


class UpdateProfileForm(FormCleanMixin):
    class Meta:
        model = Profile
        fields = ('birth_date',)
        labels = {'birth_date': 'Data urodzin'}
        widgets = {'birth_date': forms.DateInput(attrs={'type': 'date'})}


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Nowe hasło')
    # password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz nowe hasło')

    class Meta:
        model = User
        fields = ('password',)

    # def clean(self):
    #     cleaned_date = super().clean()
    #
    #     password1 = cleaned_date['password']
    #     password2 = cleaned_date['password2']
    #
    #     if password1 != password2:
    #         raise ValidationError('Hasła są różne!')
