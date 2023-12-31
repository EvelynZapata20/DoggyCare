# Generated by Django 4.2.4 on 2023-10-15 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_owner_telephone_alter_vet_telephone'),
        ('vet', '0029_alter_breed_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='dog_id',
            new_name='dog',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='clinic_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.clinic_info'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='dog_owner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.owner'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='vet_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.vet'),
        ),
    ]
