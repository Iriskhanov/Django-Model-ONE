from django.contrib import admin
from fruits.models import CheckoutCart, ChooseBerries, ChooseFruits

admin.site.register(ChooseFruits)
admin.site.register( ChooseBerries)

@admin.register(CheckoutCart)
class Fruits(admin.ModelAdmin):
    list_display = ['choose_fruits', 'basket_size', 'decorations']
