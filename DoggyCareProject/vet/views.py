from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from .models import Dog
from django.db.models import Q
from django.urls import reverse

# Create your views here.
def recomendations(request):
    return render(request, 'recomendations.html', {'recomendations': recomendations})

def dog_profile(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        form = DogRegisterForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            return redirect('dog_profile', dog_id=dog.id)
    else:
        form = DogRegisterForm(instance=dog)

    return render(request, 'dog_profile.html', {'dog': dog, 'form': form})

def dog_register(request):
    if request.method == 'POST':
        form= DogRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form= DogRegisterForm()
    return render(request, 'dog_register.html', {'form': form})

def new_record(request,dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        recordform = MedicalRecordForm(request.POST, request.FILES)
        if recordform.is_valid():
            recordform.instance.dog = dog
            recordform.save()
            return redirect(reverse('medical_record', args=[dog_id]))
    else:
        recordform = MedicalRecordForm()
    return render(request, 'new_record.html',{'dog': dog, 'recordform': recordform})


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

def medical_record(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    searchTerm = request.GET.get('searchRecord')
    if searchTerm:
        medical_record = MedicalRecord.objects.filter(
            Q(date__icontains=searchTerm) |
            Q(symptoms__icontains=searchTerm) |
            Q(appointmentType__icontains=searchTerm)|
            Q(treatment__icontains=searchTerm),
            dog=dog
        )
    else:
        medical_record = MedicalRecord.objects.filter(dog=dog)
    return render(request, 'medical_record.html', {'dog': dog, 'medical_records': medical_record})

def home(request):
    return HttpResponse('Hello, World!')