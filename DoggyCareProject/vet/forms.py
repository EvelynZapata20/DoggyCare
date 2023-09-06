from django import forms
from .models import *

class DogRegisterForm(forms.ModelForm):
    class Meta:
        model= Dog
        fields= ['image', 'owner', 'name', 'breed', 'age', 'weight', 'gender']
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model= MedicalRecord
        fields= ['dog', 'date', 'appointmentType', 'symptoms', 'treatment', 'recomendations']
        exclude=['dog']

class vaccinationCardForm(forms.ModelForm):
    class Meta:
        model = vaccination_card
        fields = "__all__"