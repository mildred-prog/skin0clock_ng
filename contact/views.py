from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    """View for contact page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
