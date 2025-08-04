"""
Product Management Widgets
Contains custom form widgets for product management forms.
Provides enhanced file input widgets with better user experience
and consistent styling across the application.
"""
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom file input widget for product image uploads.
    Extends Django's ClearableFileInput to provide a better user experience
    for image uploads. Includes custom labels and template for consistent
    styling with the rest of the application.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')

    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html'
    )
