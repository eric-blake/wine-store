from django.db import models
from django_countries.fields import CountryField

class Product(models.Model):
    title = models.CharField(max_length = 254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    grape = models.ForeignKey('Grape', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    closure = models.ForeignKey('Closure', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    # closure = models.CharField(max_length = 254, blank = True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    colour = models.ForeignKey('Colour', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    region = models.CharField(max_length = 32)
    style = models.ForeignKey('Style', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    vintage = models.IntegerField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    in_stock = models.BooleanField()
    stock_qty = models.IntegerField(null=False, blank=False)
  

    def __str__(self):
        return self.title


class Colour(models.Model):

    class Meta:
        verbose_name_plural = 'Colours'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name



class Closure(models.Model):
    class Meta:
        verbose_name_plural = 'Closure'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Style(models.Model):
    class Meta:
        verbose_name_plural = 'Styles'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Grape(models.Model):
    class Meta:
        verbose_name_plural = 'Grapes'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name