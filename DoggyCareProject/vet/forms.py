from django import forms
from .models import *


APPOINTMENT_CHOICES = [
        ('allergy evaluation', 'Allergy evaluation'),
        ('annual health exam', 'Annual health exam'),
        ('assessment of serious behavioral problems', 'Assessment of serious behavioral problems'),
        ('bladder and urinary system surgery', 'Bladder and Urinary System Surgery'),
        ('blood test', 'Blood test'),
        ('cardiology', 'Cardiology'),
        ('cardiology specialized radiology', 'Cardiology specialized radiology'),
        ('care during pregnancy and childbirth', 'Care during pregnancy and childbirth'),
        ('complete physical exam', 'Complete physical exam'),
        ('control of advanced dental diseases', 'Control of advanced dental diseases'),
        ('control of autoimmune diseases', 'Control of autoimmune diseases'),
        ('control of autoimmune diseases', 'Control of autoimmune diseases'),
        ('control of blood disorders', 'Control of blood disorders'),
        ('control of endocrine disorders', 'Control of endocrine disorders'),
        ('control of external parasites', 'Control of external parasites'),
        ('control of food allergies', 'Control of food allergies'),
        ('control of internal parasites', 'Control of internal parasites'),
        ('control of liver disorders', 'Control of liver disorders'),
        ('control of mosquito-borne diseases', 'Control of mosquito-borne diseases'),
        ('control of neuromuscular diseases', 'Control of neuromuscular diseases'),
        ('control of tick-borne diseases', 'Control of tick-borne diseases'),
        ('dental hygiene consultation', 'Dental hygiene consultation'),
        ('dental surgery', 'Dental Surgery'),
        ('dermatology', 'Dermatology'),
        ('ear surgery', 'Ear Surgery'),
        ('endocrinology', 'Endocrinology'),
        ('eye surgery', 'Eye Surgery'),
        ('evaluation of hearing problems', 'Evaluation of hearing problems'),
        ('evaluation of respiratory problems', 'Evaluation of respiratory problems'),
        ('evaluation of thyroid problems', 'Evaluation of thyroid problems'),
        ('follow-up visit after illness', 'Follow-up visit after illness'),
        ('follow-up visit after surgery', 'Follow-up visit after surgery'),
        ('gastroenterology', 'Gastroenterology'),
        ('gastrointestinal surgery', 'Gastrointestinal Surgery'),
        ('geriatric care consultation', 'Geriatric care consultation'),
        ('lameness evaluation', 'Lameness evaluation'),
        ('neonatology', 'Neonatology'),
        ('nephrology', 'Nephrology'),
        ('neutering (ovariohysterectomy)', 'Neutering (Ovariohysterectomy)'),
        ('neurology', 'Neurology'),
        ('oncology', 'Oncology'),
        ('ophthalmology', 'Ophthalmology'),
        ('oral soft tissue surgery', 'Oral Soft Tissue Surgery'),
        ('orthopedic surgery', 'Orthopedic Surgery'),
        ('orthopedics', 'Orthopedics'),
        ('physical therapy', 'Physical therapy'),
        ('psychology', 'Psychology'),
        ('reconstructive surgery', 'Reconstructive Surgery'),
        ('routine consultation', 'Routine consultation'),
        ('soft tissue surgery', 'Soft Tissue Surgery'),
        ('specialized dentistry', 'Specialized dentistry'),
        ('specialized nutrition', 'Specialized nutrition'),
        ('spaying (castration)', 'Spaying (Castration)'),
        ('spinal surgery', 'Spinal Surgery'),
        ('sterilization consultation', 'Sterilization consultation'),
        ('treatment of ear infections', 'Treatment of ear infections'),
        ('treatment of wounds and cuts', 'Treatment of wounds and cuts'),
        ('urology', 'Urology'),
        ('urine test', 'Urine test'),
        ('vaccination', 'Vaccination'),
        ('weight control and nutrition', 'Weight control and nutrition'),
        ('nose and throat surgery', 'Nose and Throat Surgery'),
        ('cardiovascular surgery', 'Cardiovascular Surgery')
        ]
fecha_actual = date.today().strftime('%Y-%m-%d')

class DogRegisterForm(forms.ModelForm):
    class Meta:
        model= Dog
        fields= ['image', 'owner', 'name', 'breed', 'birthdate', 'weight', 'gender']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model= appointment
        fields= ['date', 'time', 'appointment_type', 'dog','attended']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date', 'max': '2025-01-01' , 'min': fecha_actual}),
            'time': forms.TimeInput(attrs={'type': 'time', 'min': '06:00', 'max': '19:00'}),
            'appointment_type': forms.Select(choices=APPOINTMENT_CHOICES, attrs={'class': 'appointment-type-field'}),
            'dog': forms.Select(attrs={'class':'appointment-type-field'}),
        }
        
#medical record form for the dogs
class MedicalRecordForm(forms.ModelForm):
    class Meta:
                
        model = MedicalRecord
        fields = ['dog', 'date', 'appointmentType', 'symptoms', 'treatment', 'recommendations']
        exclude = ['dog']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date', 'max': fecha_actual, 'min': '2000-01-01'}),
            'recommendations': forms.Textarea(),
            'appointmentType': forms.Select(choices=APPOINTMENT_CHOICES, attrs={'class': 'appointment-type-field'}),
        }
class vaccinationCardForm(forms.ModelForm):
    class Meta:
        model = vaccination_card
        fields = "__all__"

class NewsForm(forms.ModelForm):
    class Meta:        
        model = news
        fields = ['header', 'body']
        widgets = {
            'body': forms.Textarea(),
        }