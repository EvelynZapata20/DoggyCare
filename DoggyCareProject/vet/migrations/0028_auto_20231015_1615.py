# Generated by Django 3.2.8 on 2023-10-15 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0027_rename_procedure_medicalrecord_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.breed'),
        ),
    ]
