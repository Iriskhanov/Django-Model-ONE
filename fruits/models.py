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
    decorations = models.CharField(max_length=255, verbose_name='оформление')
    occasion = models.CharField(max_length=255, verbose_name='повод')
    address = models.CharField(max_length=255, verbose_name='адрес доставки')
    delivery_time = models.DateTimeField(verbose_name='время доставки')
    contact_mail = models.EmailField(verbose_name='адрес почты')
    basket_size = models.CharField(max_length = 1, choices = BASKET_SIZE, verbose_name='размер корзины')
    choose_fruits = models.ForeignKey('ChooseFruits', on_delete = models.CASCADE, verbose_name='фрукты')
    choose_berries = models.ForeignKey('ChooseBerries', on_delete = models.CASCADE, verbose_name='ягоды')

    def __str__(self) -> str:
        return self.decorations

