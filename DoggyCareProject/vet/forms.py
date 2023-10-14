from django import forms
from .models import *

class DogRegisterForm(forms.ModelForm):
    class Meta:
        BREED_CHOICES = (
            ('Labrador Retriever', 'Labrador Retriever'),
            ('English Bulldog', 'English Bulldog'),
            ('Golden Retriever', 'Golden Retriever'),
            ('Rottweiler', 'Rottweiler'),
            ('Boxer', 'Boxer'),
            ('Yorkshire Terrier', 'Yorkshire Terrier'),
            ('Dachshund', 'Dachshund'),
            ('Pomeranian', 'Pomeranian'),
            ('German Shepherd', 'German Shepherd'),
            ('Chihuahua', 'Chihuahua'),
            ('Poodle', 'Poodle'),
            ('Beagle', 'Beagle'),
            ('English Bulldog', 'French Bulldog'),
            ('Shih Tzu', 'Shih Tzu'),
            ('Siberian Husky', 'Siberian Husky'),
            ('American Pit Bull Terrier', 'American Pit Bull Terrier'),
            ('Pug', 'Pug'),
            ('French Bulldog', 'French Bulldog'),
            ('Border Collie', 'Border Collie'),
            ('Australian Shepherd', 'Australian Shepherd'),
            ('Doberman Pinscher', 'Doberman Pinscher'),
            ('Cocker Spaniel', 'Cocker Spaniel'),
            ('Bull Terrier', 'Bull Terrier'),
            ('Great Dane', 'Great Dane'),
            ('Miniature Schnauzer', 'Miniature Schnauzer'),
            ('Boxer', 'Boxer'),
            ('Weimaraner', 'Weimaraner'),
            ('Papillon', 'Papillon'),
            ('Miniature Pinscher', 'Miniature Pinscher'),
            ('Jack Russell Terrier', 'Jack Russell Terrier'),
            ('Shar Pei', 'Shar Pei'),
            ('Bichon Frise', 'Bichon Frise'),
            ('Boston Terrier', 'Boston Terrier'),
            ('Shiba Inu', 'Shiba Inu'),
            ('Pekingese', 'Pekingese'),
            ('Alaskan Malamute', 'Alaskan Malamute'),
            ('Afghan Hound', 'Afghan Hound'),
            ('Basenji', 'Basenji'),
            ('Shetland Sheepdog', 'Shetland Sheepdog'),
            ('Samoyed', 'Samoyed'),
            ('Bullmastiff', 'Bullmastiff'),
            ('Akita Inu', 'Akita Inu'),
            ('American Staffordshire Terrier', 'American Staffordshire Terrier'),
            ('Borzoi', 'Borzoi'),
            ('American Eskimo Dog', 'American Eskimo Dog'),
            ('Cavalier King Charles Spaniel', 'Cavalier King Charles Spaniel'),
            ('Dalmatian', 'Dalmatian'),
            ('Lhasa Apso', 'Lhasa Apso'),
            ('Staffordshire Bull Terrier', 'Staffordshire Bull Terrier'),
            ('Rough Collie', 'Rough Collie'),
            ('Rhodesian Ridgeback', 'Rhodesian Ridgeback'),
            ('Maltese', 'Maltese'),
            ('Portuguese Water Dog', 'Portuguese Water Dog'),
            ('Miniature American Shepherd', 'Miniature American Shepherd'),
            ('Havanese', 'Havanese'),
            ('Shetland Sheepdog', 'Shetland Sheepdog'),
            ('West Highland White Terrier', 'West Highland White Terrier'),
            ('English Springer Spaniel', 'English Springer Spaniel'),
            ('Basset Hound', 'Basset Hound'),
            ('American Bulldog', 'American Bulldog'),
            ('Irish Setter', 'Irish Setter'),
            ('Leonberger', 'Leonberger'),
            ('Bloodhound', 'Bloodhound'),
            ('Doberman', 'Doberman'),
            ('Border Terrier', 'Border Terrier'),
            ('Airedale Terrier', 'Airedale Terrier'),
            ('Papillon', 'Papillon'),
            ('Tibetan Terrier', 'Tibetan Terrier'),
            ('Newfoundland', 'Newfoundland'),
            ('English Cocker Spaniel', 'English Cocker Spaniel'),
            ('Chow Chow', 'Chow Chow'),
            ('Old English Sheepdog', 'Old English Sheepdog'),
            ('Shih Tzu', 'Shih Tzu'),
            ('Australian Terrier', 'Australian Terrier'),
            ('Miniature Bull Terrier', 'Miniature Bull Terrier'),
            ('Scottish Terrier', 'Scottish Terrier'),
            ('Long-Haired Chihuahua', 'Long-Haired Chihuahua'),
            ('Rhodesian Ridgeback', 'Rhodesian Ridgeback'),
            ('German Short-Haired Pointer', 'German Short-Haired Pointer'),
            ('Belgian Malinois', 'Belgian Malinois')
        )
        model= Dog
        fields= ['image', 'owner', 'name', 'breed', 'birthdate', 'weight', 'gender']
        widgets = {
            'breed': forms.Select(choices=BREED_CHOICES, attrs={'class': 'breed-field'}),
        }
        

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        fecha_actual = date.today().strftime('%Y-%m-%d')

        APPOINTMENT_CHOICES = [
        ('allergy evaluation', 'Allergy evaluation'),
        ('annual health exam', 'Annual health exam'),
        ('assessment of serious behavioral problems', 'Assessment of serious behavioral problems'),
        ('bladder and urinary system surgery', 'Bladder and Urinary System Surgery'),
        ('blood test', 'Blood test'),
        ('cardiology', 'Cardiology'),
        ('cardiology specialized radiology', 'Cardiology specialized radiology'),
        ('care during pregnancy and childbirth', 'Care during pregnancy and childbirth'),
        ('complete physical exam', 'Complete physical exam'),
        ('control of advanced dental diseases', 'Control of advanced dental diseases'),
        ('control of autoimmune diseases', 'Control of autoimmune diseases'),
        ('control of autoimmune diseases', 'Control of autoimmune diseases'),
        ('control of blood disorders', 'Control of blood disorders'),
        ('control of endocrine disorders', 'Control of endocrine disorders'),
        ('control of external parasites', 'Control of external parasites'),
        ('control of food allergies', 'Control of food allergies'),
        ('control of internal parasites', 'Control of internal parasites'),
        ('control of liver disorders', 'Control of liver disorders'),
        ('control of mosquito-borne diseases', 'Control of mosquito-borne diseases'),
        ('control of neuromuscular diseases', 'Control of neuromuscular diseases'),
        ('control of tick-borne diseases', 'Control of tick-borne diseases'),
        ('dental hygiene consultation', 'Dental hygiene consultation'),
        ('dental surgery', 'Dental Surgery'),
        ('dermatology', 'Dermatology'),
        ('ear surgery', 'Ear Surgery'),
        ('endocrinology', 'Endocrinology'),
        ('eye surgery', 'Eye Surgery'),
        ('evaluation of hearing problems', 'Evaluation of hearing problems'),
        ('evaluation of respiratory problems', 'Evaluation of respiratory problems'),
        ('evaluation of thyroid problems', 'Evaluation of thyroid problems'),
        ('follow-up visit after illness', 'Follow-up visit after illness'),
        ('follow-up visit after surgery', 'Follow-up visit after surgery'),
        ('gastroenterology', 'Gastroenterology'),
        ('gastrointestinal surgery', 'Gastrointestinal Surgery'),
        ('geriatric care consultation', 'Geriatric care consultation'),
        ('lameness evaluation', 'Lameness evaluation'),
        ('neonatology', 'Neonatology'),
        ('nephrology', 'Nephrology'),
        ('neutering (ovariohysterectomy)', 'Neutering (Ovariohysterectomy)'),
        ('neurology', 'Neurology'),
        ('oncology', 'Oncology'),
        ('ophthalmology', 'Ophthalmology'),
        ('oral soft tissue surgery', 'Oral Soft Tissue Surgery'),
        ('orthopedic surgery', 'Orthopedic Surgery'),
        ('orthopedics', 'Orthopedics'),
        ('physical therapy', 'Physical therapy'),
        ('psychology', 'Psychology'),
        ('reconstructive surgery', 'Reconstructive Surgery'),
        ('routine consultation', 'Routine consultation'),
        ('soft tissue surgery', 'Soft Tissue Surgery'),
        ('specialized dentistry', 'Specialized dentistry'),
        ('specialized nutrition', 'Specialized nutrition'),
        ('spaying (castration)', 'Spaying (Castration)'),
        ('spinal surgery', 'Spinal Surgery'),
        ('sterilization consultation', 'Sterilization consultation'),
        ('treatment of ear infections', 'Treatment of ear infections'),
        ('treatment of wounds and cuts', 'Treatment of wounds and cuts'),
        ('urology', 'Urology'),
        ('urine test', 'Urine test'),
        ('vaccination', 'Vaccination'),
        ('weight control and nutrition', 'Weight control and nutrition'),
        ('nose and throat surgery', 'Nose and Throat Surgery'),
        ('cardiovascular surgery', 'Cardiovascular Surgery')
        ]
        model = MedicalRecord
        fields = ['dog', 'date', 'appointmentType', 'symptoms', 'treatment', 'recommendations']
        exclude = ['dog']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date', 'max': fecha_actual, 'min': '2000-01-01'}),
            'recommendations': forms.Textarea(),
            'appointmentType': forms.Select(choices=APPOINTMENT_CHOICES, attrs={'class': 'appointment-type-field'}),
        }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model= appointment
        fields= ['date', 'time', 'appointment_type', 'dog_owner_id', 'vet_id','dog_id', 'clinic_id']
        exclude=['dog_id']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
class vaccinationCardForm(forms.ModelForm):
    class Meta:
        model = vaccination_card
        fields = "__all__"