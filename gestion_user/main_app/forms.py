from .models import User
from django import forms
from django.db import models

# class User(models.Model):
#     email_user = models.EmailField(default="google@gmail.com")
#     password = models.CharField(default="test1234")
#     class Meta:
#         model= User
#         fields=['email_user','password']

class FormRegister(forms.ModelForm): 
    nom = forms.CharField(max_length=50,label="Nom" )
    prenom = forms.CharField(max_length=50, label="Prenom")
    email_user = forms.EmailField(max_length=50, label="Email")
    password = forms.CharField(widget = forms.PasswordInput,max_length=16, label="password")

class FormConnexion(forms.ModelForm):
    email_user = forms.EmailField(label="Email")
    password = forms.CharField(label="password")
    class Meta:
        model= User
        fields=['email_user','password']