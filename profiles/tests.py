from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import Order
from profiles.models import UserProfile


class ProfileViewTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Create test user and log them in
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpass123'
        )
        self.profile = self.user.userprofile

        # Create test order
        self.order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country='NG',
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test Street',
            street_address2='Apt 1',
            county='Test State',
            date='2025-07-29',
            order_number='ORDER1234',
            original_bag='{}',
            stripe_pid='pid_test_1234'
        )
        self.order.user_profile = self.profile
        self.order.save()

    def test_profile_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_profile_view_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Profile')

    def test_profile_update_post(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('profile'), {
            'default_phone_number': '987654321',
            'default_street_address1': 'New Address',
            'default_town_or_city': 'New Town',
            'default_postcode': '54321',
            'default_country': 'NG',
        })
        self.assertRedirects(response, reverse('profile'))
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, '987654321')

    def test_order_history_view(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('order_history', args=[self.order.order_number])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, self.order.order_number)
