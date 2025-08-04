"""
Contact Form Management Views
Contains views for handling contact form submissions from users.
The contact system allows customers to send inquiries, feedback, and support
requests to the store administrators through a user-friendly form interface.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    """
    Handle contact form submissions and display the contact page.
    Manages the contact form functionality, allowing users to submit
    inquiries, feedback, or support requests. Handles both GET and POST
    requests with validation and user feedback.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for your message! We will get back to you soon.'
            )
            return redirect('contact:contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
