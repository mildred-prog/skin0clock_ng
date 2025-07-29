from django.test import TestCase
from django.urls import reverse
from products.models import Product, Category
from checkout.models import Order, OrderLineItem


class CheckoutViewsTestCase(TestCase):

    def setUp(self):
        # Create a test category
        self.category = Category.objects.create(name='Cleansers')

        # Create a test product with that category
        self.product = Product.objects.create(
            name='Purifying Gel Wash',
            price=15.00,
            sku='CLE-PURGW',
            description='A gentle gel-based cleanser',
            category=self.category,
        )

        # Add item to session bag
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()

    def test_checkout_view_get(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_success_view(self):
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='GB',
            postcode='AB12CD',
            town_or_city='Testville',
            street_address1='123 Test St',
            county='Testshire',
            original_bag='{}',
            stripe_pid='test_pid_123',
        )
        OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=1,
        )
        response = self.client.get(reverse('checkout_success', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
