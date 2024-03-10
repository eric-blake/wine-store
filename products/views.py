from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from .models import Product, Colour, Style, Grape, Favourites, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile


def all_products(request):
    """ A view to show all products"""

    products = Product.objects.all().order_by('-created')
    
    query = None
    colours = None
    styles = None
    grapes = None
    countries = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

        if 'Italy' in request.GET:
            products = products.filter(country__icontains='IT')
        if 'France' in request.GET:
            products = products.filter(country__icontains='FR')    
        if 'Australia' in request.GET:
            products = products.filter(country__icontains='AU')    
        if 'USA' in request.GET:
            products = products.filter(country__icontains='US') 
        if 'Chile' in request.GET:
            products = products.filter(country__icontains='CL') 
        if 'New Zeland' in request.GET:
            products = products.filter(country__icontains='NZ') 
            
        if '6' in request.GET:
            products = products.filter(description__icontains='6 bottle') 

        if '12' in request.GET:
            products = products.filter(description__icontains='12 bottle') 

        if 'title' in request.GET:
            products = products.filter(title__icontains='Champagne') 

        if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request,
                                ("You didn't enter any search criteria!"))
                    return redirect(reverse('products'))

                queries = Q(title__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)


    product_count = products.count()
    paginator = Paginator(products, 8)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
   
    current_sorting = f'{sort}_{direction}'

      
        
    context = {
            'products': products,
            'search_term': query,
            'current_colours': colours,
            'current_styles': styles,
            'current_grapes': grapes,
            'current_sorting': current_sorting,
            'product_count': product_count,
        }

    return render(request, 'products/products.html', context)

  
def product_detail(request, product_id):
    """ A view to show individual product details """

    favourites = False
    user_review = None
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        profile = request.user.userprofile
        user_review = Review.objects.all().filter(product=product_id, user=profile)
        if Favourites.objects.filter(user=profile, product=product).exists():
            favourites = True

    reviews = Review.objects.all().filter(product=product_id).order_by('-created')

    context = {
        'product': product,
        'favourites':favourites,
        'user_review':user_review,
        'reviews': reviews,
        'review_form':ReviewForm()
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


@login_required
def favourites(request):
    """A view to show favourite page"""

    profile = UserProfile.objects.get(user=request.user)
    favourites = Favourites.objects.filter(user=profile) 

    template = 'products/favourites.html'
    context = {
        'favourites': favourites
    }

    return render(request, template, context)


@login_required
def add_to_favourites(request, product_id):
    """Add product to favourites"""
    product = get_object_or_404(Product, pk=product_id)
    profile = UserProfile.objects.get(user=request.user)
    redirect_url = request.POST.get('redirect_url')

    if Favourites.objects.filter(user=profile, product=product).exists():
        favourite_product = Favourites.objects.filter(user=profile, product=product) 
        favourite_product.delete()
        messages.success(request, f'{product.title} removed from favourites')
    else:
        favourite_product = Favourites.objects.create(user=profile, product=product)
        messages.success(request, f'{favourite_product.product.title} added to favourites')

    return redirect(redirect_url)


@login_required
def add_review(request, product_id):
    """Add a product review"""
    product = get_object_or_404(Product, pk = product_id)
    user  = request.user.userprofile
    if request.method == "POST":
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.user = user
            review.save()
            messages.success(request, 'Your review has been added. ')

        else:
            messages.error(request, 'Something went wrong, Please try again. ')

    return redirect('product_detail', product_id)



@login_required
def edit_review(request, product_id):
    """Edit a product review"""
    review = get_object_or_404(Review, pk = product_id )
    product = review.product
    review_form = ReviewForm(instance = review)

    if request.method == "POST":
        user  = request.user.userprofile
        review_form = ReviewForm(request.POST, instance = review)
        if review_form.is_valid():
            review = review_form.save()
            messages.success(request, 'You review has been updated')
            return(redirect(reverse('product_detail', args=[product.id])))
        else:
            messages.error(request,'Something went wrong, Please try again. ')

    template = 'products/edit_review.html'
    context = {
        'review_form': review_form,
        'product': product,
        'review': review
    }

    return render(request, template, context)



@login_required
def delete_review(request, product_id):
    """Delete a product review"""
    review = get_object_or_404(Review, pk = product_id)
    review.delete()
    messages.success(request, 'Successfully deleted review')
    return redirect(reverse('products'))










