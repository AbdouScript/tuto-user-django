from django.urls import path
from . import views

urlpatterns = [
    # /app/
    path("", views.index, name = "index"),
    path("users/", views.users, name="users"),
    path("sessions/", views.sessions, name="sessions"),

]