# Generated by Django 4.2.4 on 2023-10-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0024_alter_dog_vet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
