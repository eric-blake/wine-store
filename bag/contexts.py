from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from coupons.models import Coupon
from coupons.forms import CouponForm


def bag_contents(request):
    """
     Handles the shopping cart contents
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    discount = request.session.get('discount')
    code = request.session.get('code')
    coupon_discount = 0
    apply_coupon_form = CouponForm()

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if discount:
        coupon_discount = total * Decimal(discount/100)
        total -= coupon_discount

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'coupon_discount': coupon_discount,
        'apply_coupon_form': apply_coupon_form,
        'discount': discount,
        'code': code,
    }

    return context
