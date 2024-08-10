from django.contrib import admin
from fruits.models import Address, CheckoutCart, ChooseBerries, ChooseFruits

admin.site.register(ChooseFruits)
admin.site.register( ChooseBerries)
admin.site.register(Address)

@admin.register(CheckoutCart)
class Fruits(admin.ModelAdmin):
    list_display = ['decorations', 'occasion', 'basket_size']
