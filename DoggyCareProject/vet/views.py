from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Dog
from django.db.models import Q

# Create your views here.

def recomendations(request):
    return render(request, 'recomendations.html', {'recomendations': recomendations})

def dog_register(request):
    if request.method == 'POST':
        form= DogRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form= DogRegisterForm()
    return render(request, 'dog_register.html', {'form': form})

def patients(request):
    searchTerm = request.GET.get('searchDog')
    if searchTerm:
        dogs = Dog.objects.filter(
            Q(name__icontains=searchTerm) |
            Q(owner__icontains=searchTerm) |
            Q(breed__icontains=searchTerm)
        )
    else:
        dogs = Dog.objects.all()
    
    return render(request, 'patients.html', {'dogs': dogs})

def home(request):
    return HttpResponse('Hello, World!')