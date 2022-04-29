from statistics import mode
from django.utils import timezone
from django.db import models


# Create your models here.

class user(models.Model) :
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_create = models.DateTimeField()

