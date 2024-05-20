from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm


def home(request):
    return render(request, 'core/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            auth_login(request, user)
            return redirect('Pokedex:pokemon_home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return render(request, 'core/login.html', {"error": form.errors})
    else:
        return render(request, 'core/login.html', {'form': LoginForm()})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('Pokedex:pokemon_home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


def auth_logout(request):
    logout(request)
    return redirect('Pokedex:pokemon_home')


def sobre_mi(request):
    return render(request, 'core/sobre_mi.html')
