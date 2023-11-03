from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control required'}))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={'class': 'form-control required'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control required'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')