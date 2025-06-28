from .models import Wishlist


def wishlist_count(request):
    """Add wishlist count to template context"""
    if request.user.is_authenticated:
        count = Wishlist.objects.filter(user=request.user).count()
    else:
        count = 0
    
    return {'wishlist_count': count} 