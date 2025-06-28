from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_date')
    list_filter = ('added_date', 'product__category')
    search_fields = ('user__username', 'user__email', 'product__name')
    readonly_fields = ('added_date',)
    ordering = ('-added_date',) 