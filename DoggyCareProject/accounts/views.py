from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import User, Vet, Owner
from .forms import vet_signup_form, owner_signup_form, login_form
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import LoginView
from vet.models import *
from vet.forms import *
from django.db.models import Q

def home(request):
    return render(request, 'home.html')
    
# View for the registration of a vet
class vet_signup(CreateView):
    model = User
    form_class = vet_signup_form
    template_name = 'vet_signup.html'

    # Add aditional data to the template
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vet'
        # Extract the queryset of clinics from the database
        kwargs['clinics'] = clinic_info.objects.all()
        return super().get_context_data(**kwargs)

    # Save the data in the database
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patients')
    
# View for the registration of a owner
class owner_signup(CreateView):
    model = User
    form_class = owner_signup_form
    template_name = 'owner_signup.html'

    # Add aditional data to the template
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)

    # Save the data in the database
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('my_dogs')
    
# View for the login
class login_view(LoginView):
    template_name = 'login.html'

    # Ensures the data from the parent class is preserved
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    # Ensures that the user is redirected to the correct page
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            # Redirect to the correct page depending on the user type
            if user.is_vet:
                return reverse('patients')
            elif user.is_owner:
                return reverse('my_dogs')
        else:
            return reverse('login')