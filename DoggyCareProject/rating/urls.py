from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('rating/<int:record_id>/', views.record_rating, name='record_rating'),
]