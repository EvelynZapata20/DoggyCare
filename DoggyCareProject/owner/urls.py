from django.urls import path
from . import views

urlpatterns = [   
    path('my_dogs/', views.my_dogs, name='my_dogs'),
]