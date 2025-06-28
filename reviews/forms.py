from django import forms
from .models import Review

class StarRatingWidget(forms.Widget):
    template_name = 'reviews/star_rating_widget.html'
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs = attrs or {}
        self.attrs.update({
            'class': 'star-rating-widget',
            'data-max-rating': '5'
        })
    
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['value'] = value or 0
        return context

class ReviewForm(forms.ModelForm):
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
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience with this product...'}),
        } 