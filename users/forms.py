from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='',
                               widget=forms.TextInput(attrs={'size': 64, 'placeholder': "Username"}))
    password = forms.CharField(max_length=63, label='',
                               widget=forms.PasswordInput(attrs={'size': 64, 'placeholder': 'Password'}))


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=63, label='',
                               widget=forms.TextInput(attrs={'size': 64, 'placeholder': "Username"}))
    password1 = forms.CharField(max_length=63, label='',
                                widget=forms.PasswordInput(attrs={'size': 64, 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=63, label='',
                                widget=forms.PasswordInput(attrs={'size': 64,
                                                                  'placeholder': 'Confirm your Password'}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()