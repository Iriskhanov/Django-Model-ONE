from django.db import models

class ChooseFruits(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    
class ChooseBerries(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class Address(models.Model):
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
    delivery_time = models.DateTimeField(verbose_name='время доставки')
    contact_mail = models.EmailField(verbose_name='адрес почты', unique=True)
    basket_size = models.CharField(max_length = 1, choices = BASKET_SIZE, verbose_name='размер корзины')
    choose_fruits = models.ForeignKey('ChooseFruits', on_delete = models.CASCADE, verbose_name='фрукты')
    choose_berries = models.ForeignKey('ChooseBerries', on_delete = models.CASCADE, verbose_name='ягоды')
    address = models.OneToOneField('Address', on_delete = models.CASCADE, primary_key = True, verbose_name='адрес доставки')
    def __str__(self) -> str:
        return self.decorations

