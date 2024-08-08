from django.db import models

class ChooseFruits(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    
class ChooseBerries(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class CheckoutCart(models.Model):
    BASKET_SIZE = {
        ('S', 'SMALL'),
        ('M', 'MEDIUM'),
        ('L', 'LARGE'),
    }
    decorations = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    delivery_time = models.DateTimeField()
    contact_mail = models.EmailField()
    basket_size = models.CharField(max_length = 1, choices = BASKET_SIZE)
    choose_fruits = models.ForeignKey('ChooseFruits', on_delete = models.CASCADE)
    choose_berries = models.ForeignKey('ChooseBerries', on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.decorations

