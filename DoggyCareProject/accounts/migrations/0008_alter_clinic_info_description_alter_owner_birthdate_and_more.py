# Generated by Django 4.2.4 on 2023-10-14 03:06

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_merge_20231013_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic_info',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='owner',
            name='birthdate',
            field=models.DateField(validators=[accounts.models.validate_age]),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='vet',
            name='birthdate',
            field=models.DateField(validators=[accounts.models.validate_age]),
        ),
    ]