from operator import attrgetter
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from vet.models import Dog, MedicalRecord, appointment, news
from accounts.models import *
from accounts.decorators import owner_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
@owner_required
def my_dogs(request):
    search_term = request.GET.get('searchTerm')
    filter_by = request.GET.get('filter')
    dogs = Dog.objects.filter(owner=request.user.owner)
    clinics = clinic_info.objects.all()
    if search_term:
        if filter_by == 'all':
            dogs = dogs.filter(
                Q(name__icontains=search_term) | 
                Q(vet__name__icontains=search_term) |
                Q(birthdate__icontains=search_term) | 
                Q(breed__name__icontains=search_term) | 
                Q(weight__icontains=search_term) | 
                Q(gender__icontains=search_term)
            )
        elif filter_by == 'name':
            dogs = dogs.filter(name__icontains=search_term)
        elif filter_by == 'vet':
            dogs = dogs.filter(vet__name__icontains=search_term)
        elif filter_by == 'birthdate':
            dogs = dogs.filter(birthdate__icontains=search_term)
        elif filter_by == 'breed':
            dogs = dogs.filter(breed__name__icontains=search_term)
        elif filter_by == 'weight':
            dogs = dogs.filter(weight__icontains=search_term)
        elif filter_by == 'gender':
            dogs = dogs.filter(gender__icontains=search_term)
    

    return render(request, 'my_dogs.html', {'dogs': dogs, 'clinics':clinics})


#show the clinics registers to the owners, in order by rating
@login_required 
@owner_required
def all_clinics(request):
    search_term = request.GET.get('searchClinic')
    filter_by = request.GET.get('filterClinic')
    clinics = clinic_info.objects.all().order_by('-rating')
    if search_term:
        if filter_by == 'all':
            clinics = clinics.filter(
                Q(name__icontains=search_term) | 
                Q(place__icontains=search_term)
            ).order_by('-rating')
        elif filter_by == 'name':
            clinics = clinics.filter(name__icontains=search_term).order_by('-rating')
        elif filter_by == 'place':
            clinics = clinics.filter(place__icontains=search_term).order_by('-rating')
    
    return render(request, 'all_clinics.html', {'clinics': clinics})

#show the treatments registers to the owners, showed by clinic
@login_required 
@owner_required
def clinic_treatments(request, clinic_id):
    clinic = get_object_or_404(clinic_info, pk=clinic_id)
    search_treatment_term = request.GET.get('searchTreatment')
    if search_treatment_term:
        treatments = treatment.objects.filter(
        Q(name__icontains=search_treatment_term),
        clinic_id=clinic
        )
    else:
        treatments = treatment.objects.filter(clinic_id=clinic)
    return render(request, 'clinic_treatments.html', {'clinic': clinic, 'treatments': treatments})


#show the treatments registers to the owners
@login_required 
@owner_required
def all_treatments(request):
    treatments = treatment.objects.all()
    search_treatment_term = request.GET.get('searchTreatment')
    if search_treatment_term:
        treatments = treatment.objects.filter(
        Q(name__icontains=search_treatment_term)
        )
    return render(request, 'all_treatments.html', {'treatments': treatments})

#show the news registers to the owners
@login_required 
@owner_required
def all_news(request):
    news_ = news.objects.all()
    sorted_news = sorted(news_, key=lambda x: (x.date, x.time), reverse=True)
    return render(request, 'all_news.html', {'news': news_})

#show the news registers to the owners
@login_required 
@owner_required
def appointments_o(request):
    owner_ = request.user.owner
    appointments = appointment.objects.filter(dog_owner_id=request.user.owner)
    sorted_appointments = sorted(appointments, key=attrgetter('date', 'time'))
    return render(request, 'appointments_o.html', {'appointments': appointments})


#show the gog medical record to the owner
def medical_record_o(request, dog_id):
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
    return render(request, 'medical_record_o.html', {'dog': dog, 'medical_records': medical_record})