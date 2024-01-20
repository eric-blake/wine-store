from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product, Colour

def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all().order_by('-created')
    query = None
    colours = None
    
    context = {
            'products': products,
        
        }

    return render(request, 'products/products.html', context)


   
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)