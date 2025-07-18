from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from products.models import Product
from .models import Review
from .forms import ReviewForm

# Create your views here.

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if this user has already reviewed this product
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    if existing_review:
        messages.warning(request, "You have already submitted a review for this product.")
        return redirect('product_detail', product_id=product.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.date_posted = timezone.now()
            review.save()
            messages.success(request, "Thank you! Your review has been submitted.")
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})


def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all().order_by('-date_posted')
    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews})

@user_passes_test(is_admin)
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    product_id = review.product.id
    
    if request.method == 'POST':
        review.delete()
        messages.success(request, f'Review by {review.user.username} has been deleted successfully.')
        return redirect('product_detail', product_id=product_id)
    
    return render(request, 'reviews/delete_review_confirm.html', {'review': review})
