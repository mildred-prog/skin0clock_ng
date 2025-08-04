"""
Shopping Bag Management Views
Contains views for managing the shopping bag/cart functionality.
Handles adding, removing, and adjusting items in the user's shopping
bag using session-based storage. Provides temporary storage before checkout.
"""
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """
    Display the contents of the user's shopping bag. 
    Renders the shopping bag page where users can see all items they
    have added to their cart, along with quantities, prices, and total cost.
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a product to the shopping bag with specified quantity.
    Handles adding products to the user's shopping bag. Processes POST
    requests with product ID and quantity, then stores in session. If
    product already exists, increases quantity instead of adding duplicate.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    request.session.modified = True
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of a product in the shopping bag. 
    Allows users to modify quantities of items in their shopping bag.
    If quantity is set to 0 or less, removes the item entirely.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}'
        )
    else:
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    request.session.modified = True
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove a product completely from the shopping bag.
    Handles complete removal of items from the shopping bag. Processes
    AJAX requests to remove items without page refresh and returns
    appropriate HTTP status codes.
    """
    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        request.session.modified = True
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
