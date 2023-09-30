# Generated by Django 4.2.4 on 2023-09-12 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0014_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='clinic_address',
            new_name='clinic_id',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='dog_owner_name',
            new_name='dog_owner_id',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='vet_name',
            new_name='vet_id',
        ),
    ]