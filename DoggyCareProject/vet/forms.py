from django import forms
from .models import *

class DogRegisterForm(forms.ModelForm):
    class Meta:
        model= Dog
        fields= ['image', 'owner', 'name', 'breed', 'birthdate', 'weight', 'gender']
        
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model= MedicalRecord
        fields= ['dog', 'date', 'appointmentType', 'symptoms', 'treatment', 'recommendations']
        exclude=['dog']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model= appointment
        fields= ['date', 'time', 'appointment_type', 'dog_owner_id', 'vet_id','dog_id', 'clinic_id']
        exclude=['dog_id']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
class vaccinationCardForm(forms.ModelForm):
    class Meta:
        model = vaccination_card
        fields = "__all__"