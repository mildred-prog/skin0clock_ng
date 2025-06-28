from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from reviews.models import Review
from reviews.forms import ReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    current_category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            category_name = request.GET['category']
            current_category = category_name
            products = products.filter(category__name=category_name)
            categories = Category.objects.filter(name=category_name)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))  
                 
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_category': current_category,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.all().order_by('-date_posted')
    review_form = None
    user_has_reviewed = False
    
    if request.user.is_authenticated:
        user_has_reviewed = product.reviews.filter(user=request.user).exists()
        if not user_has_reviewed:
            review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'user_has_reviewed': user_has_reviewed,
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