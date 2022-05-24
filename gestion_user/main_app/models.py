from statistics import mode
from django.utils import timezone
from django.db import models
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings


# Create your models here.

class User(models.Model) :
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_create = models.DateTimeField(default=timezone.now)
    email_user = models.EmailField(max_length=140, default='google@gmail.com')
    password = models.CharField(max_length=32, default="password")

class Session(models.Model) :
    create_date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



