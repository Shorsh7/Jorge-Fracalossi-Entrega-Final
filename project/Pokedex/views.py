from django.shortcuts import render, redirect

from . import models

from .forms import PokemonForm, EntrenadorForm

def home(request):
    query = models.Pokemon.objects.all()
    context = {"pokemons": query}
    return render(request, "Pokedex/index.html", context)

def pokemon_home(request):
    query = models.Pokemon.objects.all()
    context = {"pokemons": query}
    return render(request, "Pokemon/index.html", context)

def pokemon_create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Pokedex:pokemon_home")
        else:
            return render(request, "Pokemon/pokemon_create.html", {"error": form.errors, "form": form})
    else:
        form = PokemonForm()
        return render(request, "Pokemon/pokemon_create.html", {"form": form})

def entrenador_home(request):
    query = models.Entrenador.objects.all()
    context = {"entrenadores": query}
    return render(request, "Entrenador/index.html", context)

def entrenador_create(request):
    if request.method == "POST":
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Pokedex:entrenador_home")
        else:
            return render(request, "Entrenador/entrenador_create.html", {"error": form.errors, "form": form})
    else:
        form = EntrenadorForm()
    return render(request, "Entrenador/entrenador_create.html", {"form": form})
        
