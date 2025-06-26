from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    """Home page with featured products by category"""
    featured_categories = {
        'cleansers': 1,
        'toners': 2,
        'serums': 3,
        'moisturizers': 4,
        'sunscreens': 5,
    }
    featured_products = {}
    for key, cat_id in featured_categories.items():
        featured_products[key] = Product.objects.filter(category_id=cat_id).order_by('-rating')[:1].first()
    context = {
        'featured_products': featured_products,
    }
    return render(request, 'home/index.html', context)