from django.contrib import admin
from .models import Product, Colour, Closure, Style, Grape, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','sku','country','vintage','price','image',)

    ordering = ('price',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product','review', )

    ordering = ('-created',)


class ColourAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ClosureAdmin(admin.ModelAdmin):
    list_display = ('name',)


class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GrapeeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Closure, ClosureAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Grape, GrapeeAdmin)