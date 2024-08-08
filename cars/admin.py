from django.contrib import admin
from cars.models import Equipment, FuelType, CarBrand, Car

admin.site.register(CarBrand)
admin.site.register(FuelType)
admin.site.register(Equipment)


@admin.register(Car)
class Cars(admin.ModelAdmin):
    list_display = ['color', 'year', 'engine_volume']
    search_fields = ['color', 'year']