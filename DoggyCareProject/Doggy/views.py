from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Dog

# Create your views here.

def vet_register(request):
    if request.method == 'POST':
        form= VetRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= VetRegisterForm()
    return render(request, 'vet_register.html', {'form': form})

def dog_register(request):
    if request.method == 'POST':
        form= DogRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vet_page')
    else:
        form= DogRegisterForm()
    return render(request, 'dog_register.html', {'form': form})

def vet_page(request):
    dogs= Dog.objects.all()
    return render(request, 'vet_page.html', {'dogs': dogs})

def home(request):
    return HttpResponse('Hello, World!')
