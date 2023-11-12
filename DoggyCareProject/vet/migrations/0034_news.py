# Generated by Django 4.2.4 on 2023-11-12 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_owner_telephone_alter_vet_telephone'),
        ('vet', '0033_alter_appointment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('body', models.CharField(max_length=400)),
                ('header', models.CharField(max_length=50)),
                ('vet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.vet')),
            ],
        ),
    ]