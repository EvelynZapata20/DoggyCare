# Generated by Django 4.2.4 on 2023-11-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0032_appointment_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
