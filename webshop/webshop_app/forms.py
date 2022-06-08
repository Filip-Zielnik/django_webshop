from datetime import date

from django import forms
from .models import Profile, Address

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
    birth_date = forms.DateField(
        label='Data urodzin',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )

    class Meta:
        model = Profile
        fields = ('birth_date',)

    def clean(self):
        super(ProfileForm, self).clean()
        birth_date = self.cleaned_data.get('birth_date')
        user_age = (date.today() - birth_date).days / 365
        if user_age < 18:
            self._errors['birth_date'] = self.error_class(
                ['Musisz mieć co najmniej 18 lat żeby się zarejestrować!']
            )
        return self.cleaned_data


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ('country', 'city', 'address', 'zip_code')


# class UpdateUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#
#
# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
