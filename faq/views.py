"""
FAQ Management Views
Contains views for displaying frequently asked questions and answers.
The FAQ system provides users with quick access to common information
about the store, products, and services.
"""
from django.shortcuts import render
from .models import FAQ


def faq_list(request):
    """
    Display all frequently asked questions and answers.
    Shows all FAQ entries to help users find answers to common questions
    about the store, products, shipping, returns, and other services.
    """
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq_list.html', {'faqs': faqs})
    