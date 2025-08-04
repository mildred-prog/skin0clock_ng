"""
Product Management Models
Contains the core data models for the e-commerce product system.
Defines the structure for storing and managing product information,
categories, and related data essential for the online store functionality.
"""
from django.db import models


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

    def __str__(self):
        """Return the product name as string representation."""
        return self.name
