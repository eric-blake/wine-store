from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from .models import Product, Colour
from django.db.models import Q

def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all().order_by('-created')
    query = None
    colours = None

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
    context = {
            'products': products,
            'search_term': query,
        }

    return render(request, 'products/products.html', context)


   
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)