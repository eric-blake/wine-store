from django.contrib import admin
from .models import Product, Colour

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','country','vintage','price','image',)

    ordering = ('price',)


class ColourAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Colour, ColourAdmin)