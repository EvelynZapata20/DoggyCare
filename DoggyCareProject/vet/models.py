from django.db import models

# Create your models here, here are all the modes used in the vet app of rDoggyCare.

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
    image= models.ImageField(upload_to='images/')
    id= models.AutoField(primary_key= True)
    owner= models.CharField(blank= False, max_length=100)
    name= models.CharField(blank= False, max_length=20)
    breed= models.CharField(blank= False, max_length=20)
    age= models.CharField(blank= False, max_length=10)
    weight= models.CharField(blank= False, max_length=10)
    gender= models.CharField(blank= False, max_length=10)
    vaccination_card = models.ForeignKey(vaccination_card, on_delete=models.CASCADE,null=True,blank = True)


class MedicalRecord(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE,null=True, blank=True)
    date = models.DateField(blank = False)
    appointmentType = models.CharField(blank= False, max_length=100)
    symptoms = models.CharField(blank= False, max_length=500)
    treatment = models.CharField(blank= False, max_length=500)
    recommendations = models.CharField(blank= False, max_length=500)
    
    
    def __str__(self):
        return self.name


class appointment(models.Model):
    date = models.DateField(blank = False)
    time = models.TimeField(blank=False)
    appointment_type = models.CharField(blank= False, max_length=20)
    dog_owner_id = models.CharField(blank= False, max_length=50)
    vet_id = models.CharField(blank= False, max_length=50)
    dog_id = models.ForeignKey(Dog, on_delete=models.CASCADE,null=True, blank=True)
    clinic_id = models.CharField(blank= False, max_length=50)

    
    
    def __str__(self):
        return self.name
