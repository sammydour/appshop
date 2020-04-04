from django.contrib import admin
from .models import Product
from .models import Offer

class OfferAdmin(admin.ModelAdmin):
    
    list_display = ('code', 'name', 'price', 'discription')


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'stock')

admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)

#Register your models here.'
