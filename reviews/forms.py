"""
Product Review Management Forms
Contains forms for managing product reviews and ratings from users.
The review system allows customers to share their experiences with products,
helping other users make informed purchasing decisions.
"""
from django import forms
from .models import Review


class StarRatingWidget(forms.Widget):
    """
    Custom star rating widget for product reviews.
    Provides a user-friendly star rating interface for product reviews.
    Uses a custom template to display interactive star ratings with
    proper styling and JavaScript functionality.
    """
    template_name = 'reviews/star_rating_widget.html'

    def __init__(self, attrs=None):
        """
        Initialize the star rating widget with default attributes.
        Sets up the widget with appropriate CSS classes and data attributes
        for the star rating functionality.
        """
        super().__init__(attrs)
        self.attrs = attrs or {}
        self.attrs.update({
            'class': 'star-rating-widget',
            'data-max-rating': '5'
        })

    def get_context(self, name, value, attrs):
        """
        Get the template context for the star rating widget.
        Provides the widget context with the current rating value
        for proper display in the template.
        """
        context = super().get_context(name, value, attrs)
        context['widget']['value'] = value or 0
        return context


class ReviewForm(forms.ModelForm):
    """
    Form for submitting product reviews and ratings.
    Provides a comprehensive form for users to submit reviews including
    star ratings and text comments. Uses custom widgets for better
    user experience and proper validation.
    """
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=StarRatingWidget(),
        label='Rating'
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Share your experience with this product...'
                }
            ),
        }
