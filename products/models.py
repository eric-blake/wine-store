from django.db import models
from django_countries.fields import CountryField
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length = 254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    grape = models.CharField(max_length = 32)
    closure = models.CharField(max_length = 32)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    typeof = models.CharField(max_length = 32)
    region = models.CharField(max_length = 32)
    style = models.CharField(max_length = 254)
    vintage = models.IntegerField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    in_stock = models.BooleanField()
    stock_qty = models.IntegerField(null=False, blank=False)

def __str__(self):
    return self.name
