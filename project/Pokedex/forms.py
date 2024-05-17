from django import forms

from . import models

class PokemonForm(forms.ModelForm):
    class Meta:
        model = models.Pokemon
        fields = '__all__'

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = models.Entrenador
        fields = '__all__'
