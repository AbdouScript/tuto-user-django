from django.urls import path
from . import views

urlpatterns = [
    # /app/
    path("", views.index, name = "index"),
    path("users/", views.users, name="users"),
    path("sessions/", views.sessions, name="sessions"),
    path("<int:user_id>/details/", views.details, name="details"),
    path("auth/", views.authentification, name="auth"),

]