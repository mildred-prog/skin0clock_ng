"""
Checkout System Signals
Contains signal handlers for maintaining order totals and consistency.
These signals automatically update order totals when line items are
created, updated, or deleted to ensure data integrity.
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create.
    Automatically recalculates the order total whenever a line item
    is created or updated. Ensures order totals remain accurate
    and consistent with line item changes.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete.
    Automatically recalculates the order total when a line item
    is deleted. Ensures order totals remain accurate after item removal.
    """
    instance.order.update_total()
