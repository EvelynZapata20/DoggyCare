# Generated by Django 4.2.4 on 2023-11-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0039_vaccine_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine_info',
            name='batch_number',
            field=models.CharField(max_length=20),
        ),
    ]
