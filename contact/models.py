"""
Contact Form Management Models
Contains the model for storing contact form submissions from users.
The contact system allows customers to send inquiries, feedback, and support
requests to the store administrators.
"""
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """
    Contact form submission model for customer inquiries.
    Stores contact form submissions from users who want to reach out to
    the store for inquiries, feedback, or support. Includes customer
    information and message content with automatic timestamp tracking.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Return a descriptive string with name and date."""
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"
