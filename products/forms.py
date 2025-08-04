"""
Product Management Forms
Contains forms for managing product information in the e-commerce system.
Provides user-friendly form interfaces for creating and editing products
with proper validation and styling.
"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for creating and editing product information.
    Provides a comprehensive form for managing all product fields including
    name, description, price, category, and image uploads. Uses custom
    widgets for better user experience and includes proper styling.
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with category choices and styling.
        Populates category choices dynamically and applies consistent
        styling to all form fields for better user experience.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]

        self.fields['category'].choices = category_choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
