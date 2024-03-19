from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Coupon(models.Model):
    """
    A coupon model for discount codes to offer to customer
    """
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.code)
