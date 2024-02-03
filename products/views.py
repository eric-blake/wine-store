from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .models import Product, Colour, Style, Grape
from django.db.models import Q
from django.contrib import messages
from .forms import ProductForm


def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all().order_by('-created')
    query = None
    colours = None
    styles = None
    grapes = None
    countries = None

    if request.GET:

        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            products = products.filter(country__name__in=countries)
            countries = Product.objects.filter(name__in=countries)


        if 'colour' in request.GET:
            colours = request.GET['colour'].split(',')
            products = products.filter(colour__name__in=colours)
            colours = Colour.objects.filter(name__in=colours)


        if 'style' in request.GET:
            styles = request.GET['style'].split(',')
            products = products.filter(style__name__in=styles)
            styles = Style.objects.filter(name__in=styles)

            print(styles)


        if 'grape' in request.GET:
            grapes = request.GET['grape'].split(',')
            products = products.filter(grape__name__in=grapes)
            grapes = Grape.objects.filter(name__in=grapes)

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
            'current_colours': colours,
            'current_styles': styles,
            'current_grapes': grapes,
        }

    return render(request, 'products/products.html', context)


   
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))
    
    if request.method=="POST":
        form =ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid')

    else:
        form = ProductForm()
        
    template = 'products/add_product.html'

    context = {
        'form': form
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product')
            return(redirect(reverse('product_detail', args=[product.id])))
        else:
            messages.error(request,
                           ('Failed to update product '
                           'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted product')
    return redirect(reverse('products'))
