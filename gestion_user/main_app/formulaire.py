from email.policy import default
from django import forms

class form_auth(forms.Form):
    votre_nom = forms.CharField(label='Ton nom', max_length=100)