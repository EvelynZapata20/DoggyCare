# Generated by Django 3.2.8 on 2023-11-12 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_owner_telephone_alter_vet_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='vet',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
