from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'dealer_id', 'type', 'year')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year')


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country')
    search_fields = ('name',)
    inlines = [CarModelInline]


admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)