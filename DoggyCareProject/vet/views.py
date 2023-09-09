from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from .forms import *
from .models import Dog
from .models import vaccination_card as Vaccination


# Create your views here.

# Delete a dog
def delete_dog(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    if request.method == 'POST':
        # Delete the image file
        if dog.image:
            image_path = Path(dog.image.path)
            if image_path.exists():
                image_path.unlink()
        dog.delete()
        return redirect('patients')
    return render(request, 'dog_profile.html', {'dog': dog})

# Edit the information of a dog
def dog_profile(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    old_image = dog.image.path
    if request.method == 'POST':
        form = DogRegisterForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            # Delete the image file if it has been changed
            new_image = form.cleaned_data.get('image')
            if new_image and old_image and Path(old_image).exists():
                Path(old_image).unlink() 
            form.save()
            return redirect('dog_profile', dog_id=dog.id)
    else:
        form = DogRegisterForm(instance=dog)
    return render(request, 'dog_profile.html', {'dog': dog, 'form': form})

# Register a new dog
def dog_register(request):
    if request.method == 'POST':
        form= DogRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            new_vaccination_card = Vaccination()
            new_vaccination_card.save()
            form.instance.vaccination_card = new_vaccination_card
            form.save()
            return redirect('patients')
    else:
        form= DogRegisterForm()
    return render(request, 'dog_register.html', {'form': form})

# Show the list of dogs taking into account the search term and filters
def patients(request):
    search_term = request.GET.get('searchTerm')
    filter_by = request.GET.get('filter')
    if search_term:
        if filter_by == 'all':
            dogs = Dog.objects.filter(
                Q(name__icontains=search_term) |  Q(owner__icontains=search_term) | Q(age__icontains=search_term) |
                Q(breed__icontains=search_term) | Q(weight__icontains=search_term) | Q(gender__icontains=search_term)
            )
        elif filter_by == 'name':
            dogs =  Dog.objects.filter(name__icontains=search_term)
        elif filter_by == 'owner':
            dogs =  Dog.objects.filter(owner__icontains=search_term)
        elif filter_by == 'age':
            dogs =  Dog.objects.filter(age__icontains=search_term)
        elif filter_by == 'breed':
            dogs =  Dog.objects.filter(breed__icontains=search_term)
        elif filter_by == 'weight':
            dogs =  Dog.objects.filter(weight__icontains=search_term)
        elif filter_by == 'gender':
            dogs =  Dog.objects.filter(gender__icontains=search_term)   
    else:
        dogs = Dog.objects.all()
    return render(request, 'patients.html', {'dogs': dogs})

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

def vaccination_card(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    vaccination_card = get_object_or_404(Vaccination, pk=dog.vaccination_card_id)
    return render(request, 'vaccination_card.html', {'vaccination_card': vaccination_card , 'dog':dog})

def vaccination_card_edit(request, vac_id):
    vaccination_card = get_object_or_404(Vaccination, pk=vac_id)
    if request.method == 'POST':
        form = vaccinationCardForm(request.POST, request.FILES, instance=vaccination_card)
        if form.is_valid():
            form.save()
            return redirect(reverse('patients'))
    else:
        form = vaccinationCardForm()
    return render(request, 'vaccination_card_edit.html', {'vaccination_card_edit': vaccination_card_edit ,'form':form,})

def recomendations(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'recomendations.html', {'dog': dog,'recomendations': recomendations})

def home(request):
    return HttpResponse('Hello, World!')