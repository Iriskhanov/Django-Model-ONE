# Generated by Django 5.0.7 on 2024-08-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_car_image_alter_equipment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(choices=[('К', 'Комфорт'), ('А', 'Аукционная'), ('С', 'Стандарт'), ('Б', 'Базовая'), ('Л', 'Люкс')], max_length=1),
        ),
    ]
