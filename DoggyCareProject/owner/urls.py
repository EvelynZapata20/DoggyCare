from django.urls import path
from . import views

urlpatterns = [   
    path('my_dogs/', views.my_dogs, name='my_dogs'),
    path('all_clinics/', views.all_clinics, name='all_clinics'),
    path('clinic_treatments/<int:clinic_id>', views.clinic_treatments, name='clinic_treatments'),
    path('all_treatments/', views.all_treatments, name='all_treatments'),
    path('medical_record_o/<int:dog_id>', views.medical_record_o, name='medical_record_o'),
    path('appointments_o/', views.appointments_o, name='appointments_o'),
    path('all_news/', views.all_news, name='all_news'),
    path('vaccination_card_owner/<int:dog_id>/', views.vaccination_card_owner, name='vaccination_card_owner'),
    path('vaccination_card_info_owner/<int:vac_id>/<int:dog_id>/<int:vaccine_id>/', views.vaccination_card_info_owner, name='vaccination_card_info_owner'),
    path('recomendations_owner/<int:dog_id>/', views.recomendations_owner, name='recomendations_owner'),
]