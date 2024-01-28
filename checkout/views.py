from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OUFJkKuVsygb9R0T0yh7YSV09dRZVMihIEn4QX8pl5bqmbI9ZXFr7YM0gW0oCCHCWwVlK4Xd5v5VzmVfM8GpMNa0063P6la7I',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
