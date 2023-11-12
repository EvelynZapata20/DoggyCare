from django.db import models
from vet.models import MedicalRecord
from django.db import models
from django.db.models import Avg
from accounts.models import clinic_info
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Rating(models.Model):
    record = models.OneToOneField(MedicalRecord, on_delete=models.CASCADE, related_name='rating')
    punctuality = models.PositiveIntegerField()
    communication = models.PositiveIntegerField()    
    professionalism = models.PositiveIntegerField()
    equipment = models.PositiveIntegerField()
    service = models.PositiveIntegerField()
    transparency = models.PositiveIntegerField()


@receiver(post_save, sender=Rating)
def update_ratings(sender, instance, **kwargs):
    record = instance.record
    total_sum = (
        int(instance.punctuality) +
        int(instance.communication) +
        int(instance.professionalism) +
        int(instance.equipment) +
        int(instance.service) +
        int(instance.transparency)
    )
    total_rating = total_sum / 6
    record.r_rating = total_rating
    record.save(update_fields=['r_rating'])

    vet = record.dog.vet
    average_ratings = Rating.objects.filter(record__dog__vet=vet).aggregate(
            Avg('punctuality'),
            Avg('communication'),
            Avg('professionalism'),
            Avg('equipment'),
            Avg('service'),
            Avg('transparency')
        )
    average_rating = sum(average_ratings.values()) / 6
    vet.rating = average_rating
    vet.save(update_fields=['rating']) 

    clinic_id= vet.clinic 
    clinic= clinic_info.objects.get(id=clinic_id)
    clinic.calculate_average_rating()
