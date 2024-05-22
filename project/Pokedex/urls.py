from django.urls import path

from Pokedex import views

app_name = 'Pokedex'

urlpatterns = [

    path('', views.home, name="home"),
    path('pokemon_create/', views.pokemon_create, name="pokemon_create"),
    path('pokemon_home/', views.pokemon_home, name="pokemon_home"),
    path('entrenador_create/', views.entrenador_create, name="entrenador_create"),
    path('entrenador_home/', views.entrenador_home, name="entrenador_home"),
    path('entrenador/<int:pk>/edit/', views.entrenador_edit, name='entrenador_edit'),
    path('pokemon/<int:pk>/edit/', views.pokemon_edit, name='pokemon_edit'),
    path('pokemon/<int:pk>/delete/', views.pokemon_delete, name='pokemon_delete'),
    path('entrenador/<int:pk>/delete/', views.entrenador_delete, name='entrenador_delete'),
]