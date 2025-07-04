from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
import stripe
from django.conf import settings

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "No products in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()

    total = 2000 

    # Set up Stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Create the payment intent
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret, 
    }

    return render(request, template, context)
