from django.db import models
from datetime import date
from accounts.models import *
from django.core.exceptions import ValidationError

# Create your models here, here are all the modes used in the vet app of rDoggyCare.

def validate_minor(value):
    if value >= date.today():
        raise ValidationError('The dog birthdate must be in the past.')
    
class breed(models.Model):
    name= models.CharField(blank= False, max_length=40)

    def __str__(self):
        return self.name

class vaccination_card(models.Model):
    id = models.AutoField(primary_key= True)
    rabies = models.BooleanField("Rabies", default= False)
    CanineDistemper = models.BooleanField("Canine Distemper", default= False)
    Parvovirus = models.BooleanField("Parvovirus", default= False)
    Adenovirus = models.BooleanField("Adenovirus(CAV-1)", default= False)
    Adenovirus_2 = models.BooleanField("Adenovirus(CAV-2)", default= False)
    Parainfluenza = models.BooleanField("Parainfluenza", default= False)
    Bordetella = models.BooleanField("Bordetella", default= False)
    LymeDisease = models.BooleanField("Lyme Disease", default= False)
    CanineInfluenza = models.BooleanField("Canine Influenza", default= False)

    def __str__(self):
        return self.name

class Dog(models.Model):
    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    )
    
    image= models.ImageField(upload_to='images/')
    id= models.AutoField(primary_key= True)
    owner= models.ForeignKey(Owner, on_delete=models.CASCADE)
    name= models.CharField(blank= False, max_length=20)
    breed= models.ForeignKey(breed, on_delete=models.CASCADE)
    birthdate= models.DateField(blank= False, validators=[validate_minor])
    weight= models.FloatField(blank= False)
    gender= models.CharField(blank= False, max_length=10, choices=GENDER_CHOICES)
    vaccination_card = models.ForeignKey(vaccination_card, on_delete=models.CASCADE,null=True,blank = True)
    vet= models.ForeignKey(Vet, on_delete=models.CASCADE)

    #This method calculate the age of the dog and return the age in months ex the dog has 1 year and 6 months, the function return 
    # 18, this calculate with the actually date and the birthdate of the dog 
    def calculate_age(self):
        today = date.today()
        delta = today - self.birthdate # Difference of time 
        age = delta.days // 30  # Suppose all the months has 30 days
        return age
    

#define the class medical record with its respective fields
class MedicalRecord(models.Model):
    id = models.AutoField(primary_key= True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField(blank = False)
    appointmentType = models.CharField(blank= False, max_length=100)
    symptoms = models.CharField(blank= False, max_length=500)
    treatment = models.CharField(blank= False, max_length=500)
    recommendations = models.CharField(blank= False, max_length=1000)
    r_rating= models.DecimalField(max_digits=3, decimal_places=2, blank= True, null=True)
    

class appointment(models.Model):
    date = models.DateField(blank = False)
    time = models.TimeField(blank=False)
    appointment_type = models.CharField(blank= False, max_length=20)
    dog_owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True, blank=True)
    vet_id = models.ForeignKey(Vet, on_delete=models.CASCADE,null=True, blank=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE,null=True, blank=True)
    clinic_id = models.ForeignKey(clinic_info, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.name


#class news(models.Model):
#    date = models.DateField(blank = False)
#    time = models.TimeField(blank=False)
#    body = models.CharField(blank= False, max_length=400)
#    vet = models.ForeignKey(Vet, on_delete=models.CASCADE,null=True, blank=True)
#    header = models.CharField(blank= False, max_length=50)    
#    
#    def __str__(self):
#        return self.name


