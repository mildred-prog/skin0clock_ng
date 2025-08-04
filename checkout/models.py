"""
Checkout System Models
Contains the core models for the checkout and order management system.
Handles the complete order lifecycle from creation to completion.
"""
import uuid
from decimal import Decimal

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    Order model for storing complete order information.
    Represents a complete order in the e-commerce system. Stores all
    customer information, delivery details, order totals, and payment
    information. Includes automatic order number generation and total
    calculation functionality.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders'
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
    )

    def _generate_order_number(self):
        """
        Creates a random, unique 32-character hexadecimal string to serve
        as the order number. Ensures uniqueness across all orders.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update order totals including delivery costs.
        Recalculates the order total by summing all line items, then
        calculates delivery costs based on order value and free delivery
        threshold. Automatically saves the updated totals.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override save method to auto-generate order number.
        Ensures that every order has a unique order number by generating
        one if it doesn't exist. Prevents duplicate order numbers.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        """Return the order number as string representation."""
        return self.order_number


class OrderLineItem(models.Model):
    """
    Individual line item within an order.
    Represents a single product line within an order, including the
    product, quantity, and calculated line total. Line total is
    automatically calculated when the item is saved.
    """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems'
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override save method to calculate line total and update order.
        Automatically calculates the line item total based on product
        price and quantity, then triggers the order total update.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """Return a descriptive string representation."""
        return (
            f'SKU {self.product.sku} on order {self.order.order_number}'
        )
