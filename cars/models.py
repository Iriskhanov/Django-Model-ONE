from django.db import models
from django.core.validators import MinValueValidator


class CarBrand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Equipment(models.Model):
    EQUIPMENT = {
        ('Б', 'Базовая'),
        ('С', 'Стандарт'),
        ('К', 'Комфорт'),
        ('Л', 'Люкс'),
        ('А', 'Аукционная'),
    }
    name = models.CharField(max_length=1, choices = EQUIPMENT)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    
    color = models.CharField(max_length=50, verbose_name= 'цвет')
    year = models.PositiveSmallIntegerField(verbose_name= 'год выпуска')
    image = models.FileField()
    engine_volume = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0, verbose_name= 'объем двигателя')
    fuel_type = models.ManyToManyField('FuelType')
    brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, blank = True, null = True)
    

    def __str__(self) -> str:
        return self.color


