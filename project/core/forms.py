from django import forms

from . import views

from . import models

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    password = forms.CharField(label='Ingresar Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = models.User
        fields = ['username', 'password', 'password2', 'profile_pic']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)