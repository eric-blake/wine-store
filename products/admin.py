from django.contrib import admin
from .models import Product, Colour, Closure

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','country','vintage','price','image',)

    ordering = ('price',)


class ColourAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ClosureAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Closure, ClosureAdmin)