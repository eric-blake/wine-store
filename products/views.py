from django.shortcuts import render
from django.views import generic, View
from .models import Product

class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.filter(all)
    template_name = "products/products.html"
