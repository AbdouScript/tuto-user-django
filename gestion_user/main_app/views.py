from django.shortcuts import render
from django.http import HttpResponse
from .models import user


# Create your views here.


def index(request):
    list_users= user.objects.get(pk=1)
    return HttpResponse("Bienvenue monsieur %s" %list_users.nom)

def details(request):
    return HttpResponse("You are in details")