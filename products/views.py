from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def home(request):
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

def category_products(request, category_id):
    """A view to show all products in a specific category"""
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category_id=category_id)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/category_products.html', context)