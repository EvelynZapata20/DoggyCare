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
    path('vaccination_card_edit/<int:vac_id>/<int:dog_id>/<int:vaccine>/', views.vaccination_card_edit, name='vaccination_card_edit'),
    path('show_clinic/', views.show_clinic, name='show_clinic'),
    path('treatments/<int:clinic_id>', views.treatments, name='treatments'),
    path('new_treatment/<int:clinic_id>', views.new_treatment, name='new_treatment'),
    path('edit_treatment/<int:clinic_id>/<int:treatment_id>/', views.edit_treatment, name='edit_treatment'),
    path('delete_treatment/<int:treatment_id>/', views.delete_treatment, name='delete_treatment'),
    path('edit_clinic/<int:clinic_id>/', views.edit_clinic, name='edit_clinic'),
    path('statics/', views.statistics, name='statistics'),
    path('owners_select/', views.owners_select, name='owners_select'),
    path('new_appointment/<int:owner_id>/', views.new_appointment, name='new_appointment'),
    path('manage_appointment/<int:appointment_id>/', views.manage_appointment_view, name='manage_appointment'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('news/', views.news_view, name='news'),
    path('new_news/', views.new_news, name='new_news'),
    path('manage_news/<int:new_id>/', views.manage_news, name='manage_news'),
    path('delete_news/<int:new_id>/', views.delete_news, name='delete_news'),
    
]