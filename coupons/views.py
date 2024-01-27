from django.shortcuts import redirect
from .models import Coupon



# Coupon code learnings from https://www.youtube.com/watch?v=_dSCGMJcoe4

def apply_coupon(request):
    """Apply coupon code"""
    # now = timezone.now()
    if request.method == 'POST':
        code = request.POST.get('code')
        try: 
            code = Coupon.objects.get(code__iexact=code, 
                                        # valid_from__lte=now, 
                                        # valid_to__gte=now, 
                                      )
            if code.active:
                discount = code.discount            
                request.session['discount'] = discount
     
        except Coupon.DoesNotExist:
            request.session['discount'] = None
    return redirect('view_bag')
