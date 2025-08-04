"""
Wishlist Context Processor
Contains a context processor that provides wishlist count information
to all templates. Makes wishlist count available across the site for
display in navigation and other UI elements.
"""
from .models import Wishlist


def wishlist_count(request):
    """
    Add wishlist count to template context.
    Provides the count of items in the user's wishlist to all templates.
    Returns 0 for unauthenticated users. Used for displaying wishlist
    count in navigation and other UI elements.
    """
    if request.user.is_authenticated:
        count = Wishlist.objects.filter(user=request.user).count()
    else:
        count = 0

    return {'wishlist_count': count}
