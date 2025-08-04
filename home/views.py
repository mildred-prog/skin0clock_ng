"""
Home Page Views
Contains views for the main home page of the e-commerce site.
The home page showcases featured products from different categories to
provide users with a curated selection of the best products.
"""
from django.shortcuts import render
from products.models import Product


def index(request):
    """
    Display the home page with featured products by category.
    Creates a homepage showcasing the highest-rated product from each
    major skincare category. Provides users with a curated selection
    of the best products to encourage browsing and purchases.
    """
    featured_categories = {
        'cleansers': 1,
        'toners': 2,
        'serums': 3,
        'moisturizers': 4,
        'sunscreens': 5,
    }
    featured_products = {}
    for key, cat_id in featured_categories.items():
        featured_products[key] = Product.objects.filter(
            category_id=cat_id
        ).order_by('-rating')[:1].first()

    context = {
        'featured_products': featured_products,
    }
    return render(request, 'home/index.html', context)
