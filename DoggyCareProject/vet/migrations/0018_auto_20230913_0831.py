# Generated by Django 3.2.8 on 2023-09-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0017_alter_medicalrecord_recommendations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='age',
        ),
        migrations.AddField(
            model_name='dog',
            name='birthdate',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
    ]