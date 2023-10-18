from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import User, Vet, Owner, validate_numeric, clinic_info, treatment
from .models import User, Vet, Owner, validate_numeric, validate_age
from django import forms

#form for the vet register
class vet_signup_form(UserCreationForm):
    # fields for user
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    # fields for vet
    identification = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    name = forms.CharField(widget=forms.TextInput())
    birthdate = forms.DateField(validators=[validate_age])
    telephone = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    specialty = forms.ChoiceField(widget=forms.TextInput(), choices= Vet.SPECIALTY_CHOICES)
    experience = forms.IntegerField()
    clinic = forms.IntegerField()

    # allows the form to inherit metadata from the base in Django form for user registration.
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # ensures that all the database operations within this method are treated as a single unit
    @transaction.atomic
    # saves the user and vet data in the database
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vet = True
        if commit:
            user.save()
        vet = Vet.objects.create(user=user, identification=self.cleaned_data.get('identification'), name=self.cleaned_data.get('name'), birthdate=self.cleaned_data.get('birthdate'), telephone=self.cleaned_data.get('telephone'), specialty=self.cleaned_data.get('specialty'), experience=self.cleaned_data.get('experience'), clinic=self.cleaned_data.get('clinic'))
        return user

#form for the clinics register
class clinicRegisterForm(forms.ModelForm):
    class Meta:
        model= clinic_info
        fields= ['name', 'address', 'place', 'phone', 'description', 'opening_hours', 'rating', 'image', 'vet']

#form for the treatment register
class treatmentRegisterForm(forms.ModelForm):
    class Meta:
        model= treatment
        fields= ['name', 'description', 'duration', 'price', 'aviability', 'clinic_id']
        exclude = ['clinic_id']
        widgets = {
            'aviability': forms.CheckboxInput(attrs={'class': 'check-box'}),
        }

# form for the owner register
class owner_signup_form(UserCreationForm):
    # fields for user
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    # fields for owner
    identification = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    name = forms.CharField(widget=forms.TextInput())
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), validators=[validate_age])
    telephone = forms.CharField(widget=forms.TextInput(), validators=[validate_numeric])
    address = forms.CharField(widget=forms.TextInput())

    # allows the form to inherit metadata from the base in Django form for user registration.
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    # ensures that all the database operations within this method are treated as a single unit
    @transaction.atomic
    # saves the user and owner data in the database
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        owner = Owner.objects.create(user=user, identification=self.cleaned_data.get('identification'), name=self.cleaned_data.get('name'), birthdate=self.cleaned_data.get('birthdate'), telephone=self.cleaned_data.get('telephone'), address=self.cleaned_data.get('address'))
        return user

# form for the login
class login_form(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())




