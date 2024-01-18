from django.shortcuts import render
from django.views import generic, View
from .models import Product, Colour

def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all()
    query = None
    colours = None
    
    context = {
            'products': products,
        
        }

    return render(request, 'products/products.html', context)