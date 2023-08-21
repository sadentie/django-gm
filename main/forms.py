from .models import Goals
from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class GoalsForm(ModelForm):
    class Meta:
        model = Goals
        fields = ['goal', 'dateend']
        widgets = {
            'dateend': forms.DateInput(attrs={'type':'date'})
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    logusername= forms.CharField()
    logpassword= forms.CharField(widget=forms.PasswordInput)
