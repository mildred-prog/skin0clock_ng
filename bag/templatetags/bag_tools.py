"""
Shopping Bag Template Tags
Contains custom template tags for shopping bag functionality.
Provides template filters for calculating bag totals and other
bag-related calculations in templates.
"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal for a product line item.
    """
    return price * quantity
