from django.contrib import admin
from .models import Product
from .models import Offer
from .models import Blog

class OfferAdmin(admin.ModelAdmin):
    
    list_display = ('code', 'name', 'price', 'discription')


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'stock')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('edit', 'date')

admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Blog, BlogAdmin)


#Register your models here.'
