from django.urls import path
from . import views

urlpatterns = [   
    path('patients/', views.patients, name='patients'),
    path('appointments/', views.appointments, name='appointment'),
    path('medical_record/<int:dog_id>/', views.medical_record, name='medical_record'),
    path('dog_register/', views.dog_register, name='dog_register'),
    path('new_record/<int:dog_id>/', views.new_record, name='new_record'),
    path('edit_medical_record/<int:dog_id>/<int:record_id>/', views.edit_medical_record, name='edit_medical_record'),
    path('dog_profile/<int:dog_id>/', views.dog_profile, name='dog_profile'),
    path('delete_dog/<int:dog_id>/', views.delete_dog, name='delete_dog'),
    path('recomendations/<int:dog_id>/', views.recomendations, name='recomendations'),
    path('vaccination_card/<int:dog_id>/', views.vaccination_card, name='vaccination_card'),
    path('vaccination_card_edit/<int:vac_id>/', views.vaccination_card_edit, name='vaccination_card_edit'),
]