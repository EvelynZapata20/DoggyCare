# Generated by Django 4.2.4 on 2023-10-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_clinic_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vet',
            name='clinic',
            field=models.IntegerField(),
        ),
    ]
