from django.shortcuts import render
from products.models import Product

def index(request):
    """ A view to return the index page"""

    products = Product.objects.filter(in_stock=True).order_by('-created')[:8]
    
    context = {
            'products': products,
        
        }

    return render(request, 'home/index.html', context)
