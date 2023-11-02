from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import PasswordChangeForm, PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User, Vet, Owner
from .forms import vet_signup_form, owner_signup_form, login_form, vet_update_form, owner_update_form
from vet.models import *
from vet.forms import *


# View for the home page
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
        
# form to manage the vet account configuration
@login_required
def manage_vet(request):
    vet = Vet.objects.get(user=request.user)
    form = vet_update_form(instance=vet)
    form2 = PasswordChangeForm(request.user)

    if request.method == 'POST':
        # Verify if the submmited form is the update account form
        if 'update_account' in request.POST:
            form = vet_update_form(request.POST, instance=vet)
            if form.is_valid():
                form.save()
                return redirect('manage_vet') 
            
        # Verify if the submmited form is the change password form
        elif 'change_password' in request.POST:
            form2 = PasswordChangeForm(request.user, request.POST)
            if form2.is_valid():
                user = form2.save()
                messages.success(request, 'Your password was successfully updated!')
                return redirect('manage_vet')

    return render(request, 'manage_vet.html', {'form': form, 'form2': form2})


# form to manage the vet account configuration
@login_required
def manage_owner(request):
    owner = Owner.objects.get(user=request.user)
    form = owner_update_form(instance=owner)
    form2 = PasswordChangeForm(request.user)

    if request.method == 'POST':
        # Verify if the submmited form is the update account form
        if 'update_account' in request.POST:
            form = owner_update_form(request.POST, instance=owner)
            if form.is_valid():
                form.save()
                return redirect('manage_owner') 
            
        # Verify if the submmited form is the change password form
        elif 'change_password' in request.POST:
            form2 = PasswordChangeForm(request.user, request.POST)
            if form2.is_valid():
                user = form2.save()
                messages.success(request, 'Your password was successfully updated!')
                return redirect('manage_owner')

    return render(request, 'manage_owner.html', {'form': form, 'form2': form2})