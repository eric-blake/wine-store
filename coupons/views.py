from django.shortcuts import redirect
from .models import Coupon
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


# Coupon code concept from https://www.youtube.com/watch?v=_dSCGMJcoe4
def apply_coupon(request):
    """Apply coupon code"""
    now = timezone.now()
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            code = Coupon.objects.get(code__iexact=code)
            if code.active and code.valid_from <= now and code.valid_to >= now:
                discount = code.discount
                request.session['discount'] = discount
            elif (code.active and code.valid_to < now):
                messages.error(request, 'This code has expired.')
            else:
                messages.error(request, 'Invalid code.')

        except ObjectDoesNotExist:
            request.session['discount'] = None
            messages.error(request, 'Code does not exist')

    return redirect('view_bag')


def remove_coupon(request):
    """Remove coupon code"""
    if 'discount' in request.session:
        try:
            del request.session['discount']
        except KeyError:
            messages.error(request, 'This code not removed')

    else:
        messages.error(request, 'No code')
    return redirect('view_bag')
