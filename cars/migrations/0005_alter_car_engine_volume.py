# Generated by Django 5.0.7 on 2024-08-06 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine_volume',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='объем двигателя'),
        ),
    ]
