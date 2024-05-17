from django.urls import path

from . import views

app_name = 'core'

app_name = 'Pokedex'

urlpatterns = [
    path("", views.home, name="home"),
]