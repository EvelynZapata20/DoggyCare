"""DoggyCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vet import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)