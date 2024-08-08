# Generated by Django 5.0.7 on 2024-08-06 14:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0003_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField()),
                ('image', models.FileField(upload_to='')),
                ('engine_volume', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand')),
                ('fuel_type', models.ManyToManyField(to='cars.fueltype')),
            ],
        ),
    ]