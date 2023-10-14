from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_vet = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError('Este campo solo puede contener números.')
    

class Vet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='vet')
    identification = models.CharField(max_length=10, validators=[validate_numeric])
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    telephone = models.CharField(max_length=15, validators=[validate_numeric])
    speciality = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    clinic = models.IntegerField()
    

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='owner')
    identification = models.CharField(max_length=10, validators=[validate_numeric])
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    telephone = models.CharField(max_length=15, validators=[validate_numeric])
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class clinic_info(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(blank= False, max_length=50)
    address = models.CharField(blank= False, max_length=50)
    phone = models.CharField(blank= False, max_length=50)
    description = models.TextField(blank= False, max_length=300)
    opening_hours = models.CharField(blank= False, max_length=200)
    rating = models.FloatField(blank= False)
    image= models.ImageField(upload_to='images/')
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name

class treatment(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(blank= False, max_length=50)
    description = models.TextField(blank= False, max_length=300)
    duration = models.CharField(blank= False, max_length=100)
    price = models.CharField(blank= False, max_length=30)
    aviability = models.BooleanField(default=False)
    clinic_id = models.ForeignKey(clinic_info, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name