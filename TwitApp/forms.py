from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Twitter


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,help_text="Это обезателное поле")

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")


class LoginForm(AuthenticationForm):
    pass

class TweetForm(forms.ModelForm):

    class Meta:
        model = Twitter
        fields = ['text']