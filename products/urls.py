from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path(
        '<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),
    path(
        'category/cleansers/',
        views.category_products,
        {'category_id': 1},
        name='category_cleansers'
    ),
    path(
        'category/toners/',
        views.category_products,
        {'category_id': 2},
        name='category_toners'
    ),
    path(
        'category/serums/',
        views.category_products,
        {'category_id': 3},
        name='category_serums'
    ),
    path(
        'category/moisturizers/',
        views.category_products,
        {'category_id': 4},
        name='category_moisturizers'
    ),
    path(
        'category/sunscreens/',
        views.category_products,
        {'category_id': 5},
        name='category_sunscreens'
    ),
    path('add/', views.add_product, name='add_product'),
    path(
        'edit/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
]
