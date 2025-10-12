"""
Product Management Models
Contains the core data models for the e-commerce product system.
Defines the structure for storing and managing product information,
categories, and related data essential for the online store functionality.
"""
from django.db import models
from django.db.models import Avg, Count


class Category(models.Model):
    """
    Product category model for organizing products.
    Represents product categories that help organize and classify products
    in the e-commerce system. Provides hierarchical structure for browsing
    and filtering products, improving user experience and product discovery.
    """
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'category'

    def __str__(self):
        """Return the category name as string representation."""
        return self.name


class Product(models.Model):
    """
    Product model for storing product information.
    Represents individual products in the e-commerce system. Stores all
    essential product information including name, description, pricing,
    category association, and media files.
    """
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )

    def get_average_rating(self):
        """
        Calculate the average rating from all reviews for this product.
        Returns the average rating rounded to 2 decimal places,
        or None if no reviews exist.
        """
        from reviews.models import Review
        reviews = Review.objects.filter(product=self)
        
        if reviews.exists():
            avg_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
            return round(avg_rating, 2)
        return None

    def get_review_count(self):
        """
        Get the total number of reviews for this product.
        Returns the count of all reviews associated with this product.
        """
        from reviews.models import Review
        return Review.objects.filter(product=self).count()

    def get_rating_display(self):
        """
        Get a formatted string representation of the rating.
        Returns a string showing the rating and review count,
        or 'No reviews yet' if no reviews exist.
        """
        review_count = self.get_review_count()
        if review_count > 0:
            avg_rating = self.get_average_rating()
            return f"{avg_rating}/5 ({review_count} review{'s' if review_count != 1 else ''})"
        return "No reviews yet"

    def is_in_wishlist(self, user):
        """
        Check if this product is in the user's wishlist.
        Returns True if the product is in the user's wishlist, False otherwise.
        """
        if not user.is_authenticated:
            return False
        
        from wishlist.models import Wishlist
        return Wishlist.objects.filter(user=user, product=self).exists()

    def __str__(self):
        """Return the product name as string representation."""
        return self.name
