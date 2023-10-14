from django.urls import path
from . import views

urlpatterns = [   
    path('my_dogs/', views.my_dogs, name='my_dogs'),
    path('all_clinics/', views.all_clinics, name='all_clinics'),
    path('clinic_treatments/<int:clinic_id>', views.clinic_treatments, name='clinic_treatments'),
    path('all_treatments/', views.all_treatments, name='all_treatments'),
    path('medical_record_o/<int:dog_id>', views.medical_record_o, name='medical_record_o'),
]