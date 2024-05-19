from django.urls import path

from Pokedex import views

app_name = 'Pokedex'

urlpatterns = [

    path('', views.home, name="home"),
    path('pokemon_create/', views.pokemon_create, name="pokemon_create"),
    path('pokemon_home/', views.pokemon_home, name="pokemon_home"),
    path('entrenador_create/', views.entrenador_create, name="entrenador_create"),
    path('entrenador_home/', views.entrenador_home, name="entrenador_home"),
]