from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# USER MODELS

class CustomUser(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        verbose_name= ('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name= ('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )

    name= models.CharField(blank= False, max_length=100)
    birthday= models.DateField()
    identification= models.CharField(blank= False, max_length=10, unique= True)
    phone= models.CharField(blank= False, max_length=10)
    address= models.CharField(max_length=100)
    email= models.EmailField(blank= False, unique= True)
    password= models.CharField(blank= False, max_length=100)

    def __str__(self):
        return self.name

    
class Vet(CustomUser):
    specialty= models.CharField(blank= False, max_length=100)
    experience= models.CharField(blank= False, max_length=10)
    rating= models.FloatField(null=True)
    clinic= models.CharField(blank= False, max_length=100)

    def __str__(self):
        return self.name


# DOG MODELS

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