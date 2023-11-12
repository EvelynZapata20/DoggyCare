from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.

# User model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_vet = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

# validate numeric fields
def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError('This field must be numeric.')
    
# validate that the user is at least 18 years old
def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("You must be at least 18 years old.")

# Vet model
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
    rating= models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    
# Owner model
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

#clinics data
class clinic_info(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(blank= False, max_length=50)
    address = models.CharField(blank= False, max_length=50)
    place = models.CharField(blank= False, max_length=100)
    phone = models.CharField(blank= False, max_length=50)
    description = models.TextField(blank= False, max_length=400)
    opening_hours = models.CharField(blank= False, max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank= True, null=True)
    image= models.ImageField(upload_to='images/')
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE,null=True, blank=True)

    def calculate_average_rating(self):
        vets = Vet.objects.filter(clinic=self.id)
        total_ratings = 0
        total_vets = 0

        for vet in vets:
            if vet.rating > 0:
                total_ratings += vet.rating
                total_vets += 1

        if total_vets > 0:
            average_rating = total_ratings / total_vets
            self.rating = average_rating
            self.save(update_fields=['rating'])  
        else:
            self.rating = 0.0
            self.save(update_fields=['rating']) 

    def __str__(self):
        return self.name


#treatents data
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
        