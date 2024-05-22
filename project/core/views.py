from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm


def home(request):
    return render(request, 'core/index.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, 'core/index.html')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Formulario inválido.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('Pokedex:pokemon_home')
        else:
            form2 = CustomUserCreationForm()
            return render(request, 'core/register.html', {'form': form2,'error':form.errors})
    else:
        form = CustomUserCreationForm()
        return render(request, 'core/register.html', {'form': form})


def auth_logout(request):
    logout(request)
    form = CustomAuthenticationForm
    return render(request, 'core/login.html', {'form': form})


def aboutme(request):
    return render(request, 'core/aboutme.html')
