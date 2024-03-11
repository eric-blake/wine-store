from django.shortcuts import render, redirect,reverse,HttpResponse,get_object_or_404
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
   
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product.in_stock and quantity <= product.stock_qty:
        if item_id in list(bag.keys()):
            bag_quantity = int(bag[item_id]) + quantity
            if bag_quantity <= product.stock_qty:
                bag[item_id]= int(bag[item_id]) + quantity
                messages.success(request, f'Updated {product.title} '
                                    f'quantity to {bag[item_id]}')  
            else:
                messages.error(request, "Quantity selected not available, select lower quantity. ")
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.title} to your bag')
    else:
        messages.error(request, "Quantity selected not available, select lower quantity. ")

    request.session['bag'] = bag
    return redirect(redirect_url)
    

def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if product.in_stock and quantity <= product.stock_qty:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.title} '
                                    f'quantity to {bag[item_id]}')
            
        else:
            del bag[item_id]
            if not bag[item_id]:
                bag.pop(item_id)
            else:
                if quantity > 0:
                    bag[item_id] = quantity
                else:
                    bag.pop(item_id)
                    messages.success(request, f'Updated {product.title} '
                                    f'quantity to {bag[item_id]}')
                    
    else: 
         messages.error(request, 'Quantity selected not available, select lower quantity. ' )
         

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.title} '
                                   f'from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)