from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Wishlist
from products.models import Product


@login_required
def wishlist_view(request):
    """
    Display user's wishlist
    """
    wishlist_items = Wishlist.objects.filter(
        user=request.user
    ).select_related('product')
    return render(request, 'wishlist/wishlist.html', {
        'wishlist_items': wishlist_items
    })


@login_required
@require_POST
def add_to_wishlist(request, product_id):
    """
    Add a product to user's wishlist
    """
    product = get_object_or_404(Product, id=product_id)

    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        messages.success(
            request, f'{product.name} added to your wishlist!'
        )
    else:
        messages.info(
            request, f'{product.name} is already in your wishlist.'
        )

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': (
                f'{product.name} added to wishlist'
                if created else
                f'{product.name} already in wishlist'
            ),
            'in_wishlist': True
        })

    return redirect(request.META.get('HTTP_REFERER', 'products'))


@login_required
@require_POST
def remove_from_wishlist(request, product_id):
    """
    Remove a product from user's wishlist
    """
    product = get_object_or_404(Product, id=product_id)

    try:
        wishlist_item = Wishlist.objects.get(
            user=request.user, product=product
        )
        wishlist_item.delete()
        messages.success(
            request, f'{product.name} removed from your wishlist.'
        )

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{product.name} removed from wishlist',
                'in_wishlist': False
            })

    except Wishlist.DoesNotExist:
        messages.error(request, 'Item not found in your wishlist.')

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Item not found in wishlist'
            })

    return redirect(request.META.get('HTTP_REFERER', 'wishlist:wishlist'))


@login_required
def check_wishlist_status(request, product_id):
    """
    Check if a product is in user's wishlist (for AJAX requests)
    """
    try:
        product = Product.objects.get(id=product_id)
        in_wishlist = Wishlist.objects.filter(
            user=request.user, product=product
        ).exists()
        return JsonResponse({'in_wishlist': in_wishlist})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
