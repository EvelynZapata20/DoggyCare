from django.db import models

# Create your models here.
class Dog(models.Model):
    image= models.ImageField(upload_to='images/')
    id= models.AutoField(primary_key= True)
    owner= models.CharField(blank= False, max_length=100)
    name= models.CharField(blank= False, max_length=20)
    breed= models.CharField(blank= False, max_length=20)
    age= models.CharField(blank= False, max_length=10)
    weight= models.CharField(blank= False, max_length=10)
    gender= models.CharField(blank= False, max_length=10)
    vaccines= models.CharField(blank= False, max_length=30)
    
    def __str__(self):
        return self.name