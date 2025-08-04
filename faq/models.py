"""
FAQ Management Models
Contains the model for storing frequently asked questions and answers.
The FAQ system provides users with quick access to common information
about the store, products, and services.
"""
from django.db import models


class FAQ(models.Model):
    """
    FAQ model for storing frequently asked questions and answers.
    Stores common questions and their corresponding answers to help
    users find information quickly. Includes automatic timestamp tracking
    and is ordered by creation date for easy management.
    """
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        """Return the question as string representation."""
        return self.question
