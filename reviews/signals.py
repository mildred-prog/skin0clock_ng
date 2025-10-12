"""
Product Review Signals
Contains Django signals for automatically updating product ratings
when reviews are created, updated, or deleted.
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Review
from products.models import Product


def update_product_rating(product):
    """
    Calculate and update the average rating for a product.
    Calculates the average rating from all reviews for the product
    and updates the product's rating field. If no reviews exist,
    sets the rating to None.
    """
    reviews = Review.objects.filter(product=product)
    
    if reviews.exists():
        avg_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        product.rating = round(avg_rating, 2)
    else:
        product.rating = None
    
    product.save(update_fields=['rating'])


@receiver(post_save, sender=Review)
def update_rating_on_review_save(sender, instance, created, **kwargs):
    """
    Signal handler to update product rating when a review is saved.
    Triggers whenever a review is created or updated, ensuring the
    product's average rating stays current.
    """
    update_product_rating(instance.product)


@receiver(post_delete, sender=Review)
def update_rating_on_review_delete(sender, instance, **kwargs):
    """
    Signal handler to update product rating when a review is deleted.
    Ensures the product's average rating is recalculated when reviews
    are removed, maintaining accurate rating data.
    """
    update_product_rating(instance.product)

