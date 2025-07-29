from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQTests(TestCase):
    def setUp(self):
        self.faq1 = FAQ.objects.create(
            question="What is Skin0clock?",
            answer="Skin0clock is a skincare e-commerce platform."
        )
        self.faq2 = FAQ.objects.create(
            question="How can I contact customer support?",
            answer="You can reach us via the contact form."
        )

    def test_faq_list_view_status_code(self):
        response = self.client.get(reverse('faq_list'))
        self.assertEqual(response.status_code, 200)

    def test_faq_list_view_template_used(self):
        response = self.client.get(reverse('faq_list'))
        self.assertTemplateUsed(response, 'faq/faq_list.html')

    def test_faqs_are_displayed(self):
        response = self.client.get(reverse('faq_list'))
        self.assertContains(response, self.faq1.question)
        self.assertContains(response, self.faq2.question)
