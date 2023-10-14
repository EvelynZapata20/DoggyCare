from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from .forms import *
from .models import Dog
from accounts.models import Vet, clinic_info
from accounts.forms import *
from .models import vaccination_card as vaccination
import re
from accounts.decorators import custom_permission_required, vet_required
from accounts.decorators import vet_required
from django.contrib.auth.decorators import login_required


# Create your views here.

# Delete a dog
@login_required 
@vet_required
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

@login_required 
@vet_required
def delete_treatment(request, treatment_id):
    if request.user.is_authenticated:
        vet = Vet.objects.get(user=request.user)
        clinic_id = vet.clinic
    else:
        clinic = None
    treatment_ = get_object_or_404(treatment, pk=treatment_id)
    if request.method == 'POST':
        treatment_.delete()
        return redirect('treatments', clinic_id=clinic_id)
    return render(request, 'edit_treatment.html', {'treatment': treatment_})

# Edit the information of a dog
@login_required 
@vet_required
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


@login_required 
@vet_required
@custom_permission_required('can_manage')
def edit_clinic(request, clinic_id):
    clinic = get_object_or_404(clinic_info, pk=clinic_id)
    if request.method == 'POST':
        form = clinicRegisterForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('edit_clinic', clinic_id=clinic.id)
    else:
        form = clinicRegisterForm(instance=clinic)

    return render(request, 'edit_clinic.html', {'clinic': clinic, 'form': form})

#edit an existing medical record for any dog
@login_required 
@vet_required
def edit_medical_record(request, dog_id, record_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    record = get_object_or_404(MedicalRecord, pk=record_id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('edit_medical_record', dog_id=dog.id, record_id=record.id)
    else:
        form = MedicalRecordForm(instance=record)
    return render(request, 'edit_medical_record.html', {'dog': dog, 'form': form})


@login_required 
@vet_required
@custom_permission_required('can_manage')
def edit_treatment(request, clinic_id, treatment_id):
    clinic = get_object_or_404(clinic_info, pk=clinic_id)
    treatment_ = get_object_or_404(treatment, pk=treatment_id)
    if request.method == 'POST':
        form = treatmentRegisterForm(request.POST, request.FILES, instance=treatment_)
        if form.is_valid():
            form.save()
            return redirect('edit_treatment', clinic_id=clinic.id, treatment_id=treatment_.id)
    else:
        form = treatmentRegisterForm(instance=treatment_)
    return render(request, 'edit_treatment.html', {'clinic': clinic, 'treatment': treatment_, 'form': form})

# Register a new dog
@login_required 
@vet_required
def dog_register(request):
    if request.method == 'POST':
        form= DogRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.vet = request.user.vet
            new_vaccination_card = vaccination()
            new_vaccination_card.save()
            form.instance.vaccination_card = new_vaccination_card
            form.save()
            return redirect('patients')
    else:
        form= DogRegisterForm()
    return render(request, 'dog_register.html', {'form': form})

# Show the list of dogs taking into account the search term and filters
@login_required 
@vet_required
def patients(request):
    search_term = request.GET.get('searchTerm')
    filter_by = request.GET.get('filter')
    dogs = Dog.objects.filter(vet=request.user.vet)
    if search_term:
        if filter_by == 'all':
            dogs = dogs.filter(
                Q(name__icontains=search_term) | 
                Q(owner__name__icontains=search_term) |
                Q(birthdate__icontains=search_term) | 
                Q(breed__name__icontains=search_term) | 
                Q(weight__icontains=search_term) | 
                Q(gender__icontains=search_term)
            )
        elif filter_by == 'name':
            dogs = dogs.filter(name__icontains=search_term)
        elif filter_by == 'owner':
            dogs = dogs.filter(owner__name__icontains=search_term)
        elif filter_by == 'birthdate':
            dogs = dogs.filter(birthdate__icontains=search_term)
        elif filter_by == 'breed':
            dogs = dogs.filter(breed__name__icontains=search_term)
        elif filter_by == 'weight':
            dogs = dogs.filter(weight__icontains=search_term)
        elif filter_by == 'gender':
            dogs = dogs.filter(gender__icontains=search_term)

    return render(request, 'patients.html', {'dogs': dogs})


# Show the clinic of each vet
@login_required 
@vet_required
def show_clinic(request):
    user_has_permission = request.user.has_perm("accounts.can_manage")
    if request.user.is_authenticated:
        vet = Vet.objects.get(user=request.user)
        clinic_id = vet.clinic
        clinic = clinic_info.objects.filter(id=clinic_id).first()
    else:
        clinic = None
    return render(request, 'show_clinics.html', {'clinics': clinic, 'user_has_permission': user_has_permission})

#create a new medical_record register for any dog
@login_required 
@vet_required
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

@login_required 
@vet_required
def new_treatment(request,clinic_id):
    clinic = get_object_or_404(clinic_info, pk=clinic_id)
    if request.method == 'POST':
        recordform = treatmentRegisterForm(request.POST, request.FILES)
        if recordform.is_valid():
            recordform.instance.clinic_id = clinic
            recordform.save()
            return redirect(reverse('treatments', args=[clinic_id]))
    else:
        recordform = treatmentRegisterForm()
    return render(request, 'new_treatment.html',{'clinics': clinic, 'recordform': recordform})

#show the medical_record registers by different filters, in order from most recent to oldest
@login_required 
@vet_required
def medical_record(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    filter_by = request.GET.get('filterRecord')
    search_record_term = request.GET.get('searchRecord')
    if search_record_term:
        if filter_by == 'all':
            medical_record = MedicalRecord.objects.filter(
                Q(date__icontains=search_record_term) |
            Q(symptoms__icontains=search_record_term) |
            Q(appointmentType__icontains=search_record_term)|
            Q(treatment__icontains=search_record_term) |
            Q(recommendations__icontains=search_record_term),
            dog=dog
            ).order_by('-date')
        elif filter_by == 'date':
            medical_record =  MedicalRecord.objects.filter(date__icontains=search_record_term,dog=dog).order_by('-date')
        elif filter_by == 'appointmentType':
            medical_record =  MedicalRecord.objects.filter(appointmentType__icontains=search_record_term,dog=dog).order_by('-date')
        elif filter_by == 'symptoms':
            medical_record =  MedicalRecord.objects.filter(symptoms__icontains=search_record_term,dog=dog).order_by('-date')
        elif filter_by == 'treatment':
            medical_record =  MedicalRecord.objects.filter(treatment__icontains=search_record_term,dog=dog).order_by('-date')
        elif filter_by == 'recommendations':
            medical_record =  MedicalRecord.objects.filter(recommendations__icontains=search_record_term,dog=dog).order_by('-date')
    else:
        medical_record = MedicalRecord.objects.filter(dog=dog).order_by('-date')
    return render(request, 'medical_record.html', {'dog': dog, 'medical_records': medical_record})

@login_required 
@vet_required
def treatments(request, clinic_id):
    clinic = get_object_or_404(clinic_info, pk=clinic_id)
    search_record_term = request.GET.get('searchTreatment')
    user_has_permission = request.user.has_perm("accounts.can_manage")
    if search_record_term:
        treatments = treatment.objects.filter(
        Q(name__icontains=search_record_term),
        clinic_id=clinic
        )
    else:
        treatments = treatment.objects.filter(clinic_id=clinic)
    return render(request, 'treatments.html', {'clinics': clinic, 'treatments': treatments, 'user_has_permission': user_has_permission})

#show the appointments registers by different filters, in order from oldest to most recent
@login_required 
@vet_required
def appointments(request):
    return render(request, 'appointments.html', {'appointments': appointments})

@login_required 
@vet_required
def vaccination_card(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    vaccination_card = get_object_or_404(vaccination, pk=dog.vaccination_card_id)
    return render(request, 'vaccination_card.html', {'vaccination_card': vaccination_card , 'dog':dog})

@login_required 
@vet_required
def vaccination_card_edit(request, vac_id):
    vaccination_card = get_object_or_404(vaccination, pk=vac_id)
    if request.method == 'POST':
        form = vaccinationCardForm(request.POST, request.FILES, instance=vaccination_card)
        if form.is_valid():
            form.save()
            return redirect(reverse('patients'))
    else:
        form = vaccinationCardForm()
    return render(request, 'vaccination_card_edit.html', {'vaccination_card_edit': vaccination_card_edit ,'form':form,})

# This function send the dog, vaccination card and the age of the dog for generate the recomendations for each dog
@login_required 
@vet_required
def recomendations(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    vaccination_card = dog.vaccination_card_id
    vac_card = get_object_or_404(vaccination, pk=vaccination_card)
    age = dog.calculate_age()
    return render(request, 'recomendations.html', {'dog': dog,'vac_card': vac_card, 'age': age,})