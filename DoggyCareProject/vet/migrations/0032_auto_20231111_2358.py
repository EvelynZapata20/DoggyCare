# Generated by Django 3.2.8 on 2023-11-12 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0031_alter_appointment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
