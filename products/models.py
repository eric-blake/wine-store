from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from profiles.models import UserProfile
import uuid
from django.core.validators import RegexValidator, MinValueValidator
from decimal import Decimal


class Product(models.Model):
    """Class for all products"""
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator
                                            (Decimal('0.01'))])
    grape = models.ForeignKey('Grape', null=True, blank=True,
                              on_delete=models.SET_NULL)
    closure = models.ForeignKey('Closure', null=True, blank=True,
                                on_delete=models.SET_NULL)
    country = CountryField(blank_label='Country *', null=False,
                           blank=False)
    colour = models.ForeignKey('Colour', null=True, blank=True,
                               on_delete=models.SET_NULL)
    region = models.CharField(max_length=32)
    style = models.ForeignKey('Style', null=True, blank=True,
                              on_delete=models.SET_NULL)
    vintage = models.IntegerField(
        blank=False,
        validators=[RegexValidator(regex='^.{4}$',
                                   message='Enter year in YYYY format',
                                   code='nomatch')])
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    in_stock = models.BooleanField()
    stock_qty = models.PositiveIntegerField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=32, unique=True,
                           null=True, editable=False)

    def __str__(self):
        return self.title

    def _generate_sku(self):
        """
        Generate a random, unique sku number using UUID
        """
        return uuid.uuid1().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the sku number
        if it hasn't been set already.
        """
        if not self.sku:
            self.sku = self._generate_sku()
        super().save(*args, **kwargs)


class Colour(models.Model):
    """Product colour model"""

    class Meta:
        verbose_name_plural = 'Colours'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Closure(models.Model):
    """Product closure model"""
    class Meta:
        verbose_name_plural = 'Closure'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Style(models.Model):
    """Product style model"""
    class Meta:
        verbose_name_plural = 'Styles'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Grape(models.Model):
    """Product grape type model"""
    class Meta:
        verbose_name_plural = 'Grapes'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Favourites(models.Model):
    """Product favourites model"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title


class Review(models.Model):
    """ Product review model"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"Review {self.review} by {self.user}"
