from django.shortcuts import render, redirect

from . import models

from .forms import PokemonForm, EntrenadorForm

def home(request):
    query = models.Pokemon.objects.all()
    context = {"pokemons": query}
    return render(request, "Pokedex/index.html", context)

def pokemon_create(request):
    if(request.method == "POST"):
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Pokedex:pokemon_home")
        else:
            form2 = PokemonForm()
            return render(request, "Pokemon/pokemon_create.html", {"error": form.errors, "form": form2})
        
def pokemon_home(request):
    query = models.Pokemon.objects.all()
    context = {"pokemons": query}
    return render(request, "Pokedex/pokedex_home.html", context)

def entrenador_create(request):
    if(request.method == "POST"):
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Pokedex:pokemon_home")
        else:
            form2 = EntrenadorForm()
            return render(request, "Pokedex/entrenador_create.html", {"error": form.errors, "form": form2})
        
def entrenador_home(request):
    query = models.Entrenador.objects.all()
    context = {"entrenadores": query}
    return render(request, "Pokedex/entrenador_home.html", context)
