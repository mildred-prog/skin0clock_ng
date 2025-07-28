from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for contact page
    This form is used to collect user contact information and messages.
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
        super().__init__(*args, **kwargs)
        
        self.fields['name'].label = 'Name'
        self.fields['email'].label = 'Email'
        self.fields['message'].label = 'Message'
