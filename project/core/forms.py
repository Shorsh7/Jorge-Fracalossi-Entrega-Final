from django import forms

from . import views

from . import models

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    class Meta:
        model = models.User
        fields = ['username', 'password', 'password2', 'profile_pic']