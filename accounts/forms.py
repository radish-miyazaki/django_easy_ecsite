from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age', min_value=0)
    email = forms.EmailField(label='Mail address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ['username', 'age', 'email', 'password']

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data.get('password'), user)
        user.set_password(self.cleaned_data.get('password'))
        user.save()

        return user


# class UserLoginForm(forms.Form):
    # email = forms.EmailField(label='Mail address')
    # password = forms.CharField(label='Password', widget=forms.PasswordInput())

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Mail address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    remember = forms.BooleanField(label='Remember me', required=False)

