from django import forms
from django.forms import ModelForm
from .models import *

class contactforms(forms.ModelForm):

    class Meta():
        model= contact
        exclude = ["subject"]

class Newsletterforms(forms.ModelForm):
     
     class Meta:
         model = Newsletter
         fields = '__all__'