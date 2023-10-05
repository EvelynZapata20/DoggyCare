from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Vet, Owner, validate_numeric
from django import forms

class vet_signup_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    identification = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    name = forms.CharField(widget=forms.TextInput())
    birthdate = forms.DateField()
    telephone = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    speciality = forms.CharField(widget=forms.TextInput())
    experience = forms.IntegerField()
    clinic = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vet = True
        if commit:
            user.save()
        vet = Vet.objects.create(user=user, identification=self.cleaned_data.get('identification'), name=self.cleaned_data.get('name'), birthdate=self.cleaned_data.get('birthdate'), telephone=self.cleaned_data.get('telephone'), speciality=self.cleaned_data.get('speciality'), experience=self.cleaned_data.get('experience'), clinic=self.cleaned_data.get('clinic'))
        return user
    
class owner_signup_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    identification = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    name = forms.CharField(widget=forms.TextInput())
    birthdate = forms.DateField()
    telephone = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    address = forms.CharField(widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        owner = Owner.objects.create(user=user, identification=self.cleaned_data.get('identification'), name=self.cleaned_data.get('name'), birthdate=self.cleaned_data.get('birthdate'), telephone=self.cleaned_data.get('telephone'), address=self.cleaned_data.get('address'))
        return user

class login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

