from django.urls import path
from . import views

urlpatterns = [
    # /user/
    path("", views.index, name = "index"),
    path("details/", views.details, name = "details")
]