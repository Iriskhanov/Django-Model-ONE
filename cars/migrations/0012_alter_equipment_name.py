# Generated by Django 5.0.7 on 2024-08-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_equipment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(choices=[('А', 'Аукционная'), ('Б', 'Базовая'), ('С', 'Стандарт'), ('К', 'Комфорт'), ('Л', 'Люкс')], max_length=1),
        ),
    ]