from django.test import TestCase
from django.urls import reverse
from .models import Contact


class ContactViewTests(TestCase):
    def setUp(self):
        self.url = reverse('contact:contact')

    def test_contact_get(self):
        """
        Test that GET request to contact page returns 200
        and uses correct template
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIn('form', response.context)

    def test_contact_post_valid(self):
        """
        Test submitting valid contact form data creates Contact
        and redirects with success message
        """
        data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'This is a test message.',
        }
        response = self.client.post(self.url, data, follow=True)

        # Check redirect back to contact page
        self.assertRedirects(response, self.url)

        # Check success message in response context
        messages = list(response.context['messages'])
        self.assertTrue(
            any('Thank you for your message' in str(m) for m in messages)
        )

        # Check Contact object was created
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, data['name'])
        self.assertEqual(contact.email, data['email'])
        self.assertEqual(contact.message, data['message'])

    def test_contact_post_invalid(self):
        """
        Test submitting invalid contact form data re-renders form with errors
        """
        data = {
            'name': '',  # name is required
            'email': 'not-an-email',
            'message': '',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertEqual(Contact.objects.count(), 0)
