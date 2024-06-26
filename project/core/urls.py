from django.urls import path

from . import views

app_name = 'core'

app_name = 'Pokedex'

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.auth_logout, name="logout"),
    path("home/", views.home, name="home"),
    path("aboutme/", views.aboutme, name="aboutme"),
]