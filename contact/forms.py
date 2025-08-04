"""
Contact Form Management Forms
Contains forms for handling contact form submissions from users.
The contact form allows customers to send inquiries, feedback, and support
requests to the store administrators with proper validation and styling.
"""
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for contact page submissions.
    Collects user contact information and messages for customer service.
    Includes proper styling, placeholders, and validation for better
    user experience and data quality.
    """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Your Message'
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with custom labels and styling.
        Sets up form fields with appropriate labels and styling
        for consistent user experience across the contact form.
        """
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Name'
        self.fields['email'].label = 'Email'
        self.fields['message'].label = 'Message'
