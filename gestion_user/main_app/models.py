from statistics import mode
from django.utils import timezone
from django.db import models


# Create your models here.

class User(models.Model) :
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_create = models.DateTimeField()

class Session(models.Model) :
    create_date = models.DateField()
    user_date = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.choice_text
