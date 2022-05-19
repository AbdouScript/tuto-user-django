from statistics import mode
from django.utils import timezone
from django.db import models


# Create your models here.

class User(models.Model) :
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_create = models.DateTimeField(default=timezone.now)

class Session(models.Model) :
    create_date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
