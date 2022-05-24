from django.urls import path
from . import views

urlpatterns = [
    # /app/
    path("", views.index, name = "index"),
    path("users/", views.users, name="users"),
    path("sessions/", views.sessions, name="sessions"),
    path("<int:user_id>/details/", views.details, name="details"),
    # path("inscription/", views.inscription, name="inscription"),
    path("register/", views.register, name="register"),
    # path("profil/", views.profil, name="profil"),
    path("connexion/", views.connexion, name="connexion"),
    path("<int:user_id>/profil/", views.profil, name="profil"),
]