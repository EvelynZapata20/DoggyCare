from django.shortcuts import render
from django.db.models import Q
from vet.models import Dog
from accounts.decorators import owner_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
@owner_required
def my_dogs(request):
    search_term = request.GET.get('searchTerm')
    filter_by = request.GET.get('filter')
    dogs = Dog.objects.filter(owner=request.user.owner)
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

    return render(request, 'my_dogs.html', {'dogs': dogs})
