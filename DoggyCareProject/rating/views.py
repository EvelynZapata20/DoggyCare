from django.shortcuts import render, redirect
from vet.models import MedicalRecord
from .models import Rating
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def record_rating(request, record_id):
    if request.method == 'POST':
        record= MedicalRecord.objects.get(pk=record_id)
        punctuality = request.POST.get('punctuality')
        communication = request.POST.get('communication')
        professionalism = request.POST.get('professionalism')
        equipment = request.POST.get('equipment')
        service = request.POST.get('service')
        transparency = request.POST.get('transparency')
    
        Rating.objects.create(
            record=record,
            punctuality=punctuality,
            communication=communication,
            professionalism=professionalism,
            equipment=equipment,
            service=service,
            transparency=transparency
        )
        
        return redirect('medical_record_o', dog_id=record.dog.id)
    
    record= MedicalRecord.objects.get(pk=record_id)
    return render(request, 'rating.html', {'record': record})
