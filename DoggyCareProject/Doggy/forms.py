from django import forms
from .models import *

class VetRegisterForm(forms.ModelForm):
    class Meta:
        model= Vet
        fields= ['name', 'birthday', 'identification', 'phone', 'address', 'email', 'password', 'specialty', 'experience', 'clinic']

class DogRegisterForm(forms.ModelForm):
    class Meta:
        model= Dog
        fields= ['image', 'owner', 'name', 'breed', 'age', 'weight', 'gender', 'vaccines']