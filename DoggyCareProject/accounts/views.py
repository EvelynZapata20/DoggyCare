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

def home(request):
    return render(request, 'home.html')
    
# Vista para el registro de un veterinario (Vet)
class vet_signup(CreateView):
    model = User
    form_class = vet_signup_form
    template_name = 'vet_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vet'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patients')
    
# Vista para el registro de un dueño (Owner)
class owner_signup(CreateView):
    model = User
    form_class = owner_signup_form
    template_name = 'owner_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    

class login_view(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_vet:
                return reverse('patients')
            elif user.is_owner:
                return reverse('home')
        else:
            return reverse('login')