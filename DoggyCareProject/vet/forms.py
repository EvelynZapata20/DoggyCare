from django import forms
from .models import *

class DogRegisterForm(forms.ModelForm):
    class Meta:
        model= Dog
        fields= ['image', 'owner', 'name', 'breed', 'age', 'weight', 'gender']