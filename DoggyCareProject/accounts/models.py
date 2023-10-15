from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_vet = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError('This field must be numeric.')
    
    
def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("You must be at least 18 years old.")


class Vet(models.Model):
    SPECIALTY_CHOICES = (
        ('General Medicine', 'General Medicine'),
        ('Surgery', 'Surgery'),
        ('Dermatology', 'Dermatology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Dentistry', 'Dentistry'),
        ('Orthopedics', 'Orthopedics'),
        ('Internal Medicine', 'Internal Medicine'),
        ('Oncology', 'Oncology'),
        ('Rehabilitation and Physical Therapy', 'Rehabilitation and Physical Therapy'),
        ('Animal Behavior', 'Animal Behavior'),
        ('Emergency and Critical Care Medicine', 'Emergency and Critical Care Medicine'),
        ('Radiology and Diagnostic Imaging', 'Radiology and Diagnostic Imaging'),
        ('Preventive Medicine', 'Preventive Medicine'),
        ('Holistic Medicine', 'Holistic Medicine'),
    )
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='vet')
    identification = models.CharField(max_length=10, validators=[validate_numeric])
    name = models.CharField(max_length=50)
    birthdate = models.DateField(validators=[validate_age])
    telephone = models.CharField(max_length=50, validators=[validate_numeric])
    specialty = models.CharField(max_length=100, choices=SPECIALTY_CHOICES)
    experience = models.PositiveIntegerField()
    clinic = models.IntegerField()
    

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='owner')
    identification = models.CharField(max_length=10, validators=[validate_numeric])
    name = models.CharField(max_length=50)
    birthdate = models.DateField(validators=[validate_age])
    telephone = models.CharField(max_length=50, validators=[validate_numeric])
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class clinic_info(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(blank= False, max_length=50)
    address = models.CharField(blank= False, max_length=50)
    place = models.CharField(blank= False, max_length=100)
    phone = models.CharField(blank= False, max_length=50)
    description = models.TextField(blank= False, max_length=400)
    opening_hours = models.CharField(blank= False, max_length=200)
    rating = models.FloatField(blank= False)
    image= models.ImageField(upload_to='images/')
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name

class treatment(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(blank= False, max_length=50)
    description = models.TextField(blank= False, max_length=400)
    duration = models.CharField(blank= False, max_length=100)
    price = models.CharField(blank= False, max_length=30)
    aviability = models.BooleanField(default=False)
    clinic_id = models.ForeignKey(clinic_info, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name