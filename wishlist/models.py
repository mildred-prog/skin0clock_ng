"""
Wishlist Management Models

Contains the model for storing user wishlist items.
The wishlist system allows users to save products they're interested in
for future reference and purchase.
"""
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """
    Wishlist model for storing user's saved products.
    Represents items that users have added to their wishlist for future
    reference. Each user can only add a product once to prevent duplicates.
    Includes automatic timestamp tracking for when items were added.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        verbose_name_plural = 'Wishlist items'

    def __str__(self):
        """Return a descriptive string with user and product."""
        return f"{self.user.username} - {self.product.name}"
