"""
Product Review Management Models
Contains the model for storing product reviews and ratings from users.
The review system allows customers to share their experiences with products,
helping other users make informed purchasing decisions.
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Product review model for customer feedback and ratings.
    Stores customer reviews and ratings for products. Each user can only
    submit one review per product to prevent spam and ensure authenticity.
    Reviews include both numerical ratings and text comments with timestamps.
    """
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product', 'user']

    def __str__(self):
        """Return a descriptive string with user and product."""
        return (
            f"Review by {self.user.username} on {self.product.name}"
        )
