from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'date_posted', 'comment_preview')
    list_filter = ('rating', 'date_posted', 'product__category')
    search_fields = ('user__username', 'user__email', 'product__name', 'comment')
    readonly_fields = ('date_posted',)
    ordering = ('-date_posted',)
    
    def comment_preview(self, obj):
        return obj.comment[:100] + '...' if len(obj.comment) > 100 else obj.comment
    comment_preview.short_description = 'Comment Preview'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'product')
