from django.shortcuts import render, redirect, get_object_or_404

from . import models

from .forms import PokemonForm, EntrenadorForm

def home(request):
    query = models.Pokemon.objects.all()
    context = {"pokemons": query}
    return render(request, "Pokedex/index.html", context)

def pokemon_home(request):
    query = models.Pokemon.objects.all()
    context = {"pokemons": query}
    if request.user.is_superuser:
        return render(request, "Pokemon/index_admin.html", context)
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
    if request.user.is_superuser:
        return render(request, "Entrenador/index_admin.html", context)
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

def entrenador_edit(request, pk):
    entrenador = get_object_or_404(models.Entrenador, pk=pk)
    if request.method == "POST":
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect("Pokedex:entrenador_home")
        else:
            return render(request, "Entrenador/entrenador_create.html", {"form": form, "error": form.errors})
    else:
        form = EntrenadorForm(instance=entrenador)
        return render(request, "Entrenador/entrenador_create.html", {"form": form})
    
def pokemon_edit(request, pk):
    pokemon = get_object_or_404(models.Pokemon, pk=pk)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("Pokedex:pokemon_home")
        else:
            return render(request, "Pokemon/pokemon_create.html", {"form": form, "error": form.errors})
    else:
        form = PokemonForm(instance=pokemon)
        return render(request, "Pokemon/pokemon_create.html", {"form": form})
    
def pokemon_delete(request, pk):
    pokemon = get_object_or_404(models.Pokemon, pk=pk)
    if request.method == "POST":
        pokemon.delete()
        return redirect("Pokedex:pokemon_home")
    return render(request, "Pokemon/index.html", {"pokemons": models.Pokemon.objects.all()})

def entrenador_delete(request, pk):
    entrenador = get_object_or_404(models.Entrenador, pk=pk)
    if request.method == "POST":
        entrenador.delete()
        return redirect("Pokedex:entrenador_home")
    return render(request, "Entrenador/index.html", {"entrenadores": models.Entrenador.objects.all()})
