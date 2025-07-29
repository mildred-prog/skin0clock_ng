from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Product, Category
from wishlist.models import Wishlist
from wishlist.context_processors import wishlist_count


class WishlistTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Serums')
        self.product = Product.objects.create(
            name='Vitamin C Serum',
            description='Brightens skin',
            price=25.00,
            category=self.category,
            rating=4.5,
        )

    def test_redirect_anonymous_user_from_wishlist_view(self):
        response = self.client.get(reverse('wishlist:wishlist'))
        self.assertRedirects(response, f"/accounts/login/?next={reverse('wishlist:wishlist')}")

    def test_redirect_anonymous_user_from_add_view(self):
        response = self.client.post(reverse('wishlist:add_to_wishlist', args=[self.product.id]))
        self.assertRedirects(response, f"/accounts/login/?next={reverse('wishlist:add_to_wishlist', args=[self.product.id])}")

    def test_add_to_wishlist_once(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('wishlist:add_to_wishlist', args=[self.product.id]), follow=True)
        self.assertEqual(Wishlist.objects.count(), 1)
        self.assertContains(response, 'added to your wishlist')

    def test_add_same_product_twice(self):
        self.client.login(username='testuser', password='testpass')
        self.client.post(reverse('wishlist:add_to_wishlist', args=[self.product.id]))
        response = self.client.post(reverse('wishlist:add_to_wishlist', args=[self.product.id]), follow=True)
        self.assertEqual(Wishlist.objects.count(), 1)
        self.assertContains(response, 'already in your wishlist')

    def test_remove_nonexistent_item(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('wishlist:remove_from_wishlist', args=[self.product.id]), follow=True)
        self.assertContains(response, 'Item not found in your wishlist')

    def test_wishlist_context_processor_logged_in(self):
        self.client.login(username='testuser', password='testpass')
        Wishlist.objects.create(user=self.user, product=self.product)
        request = self.factory.get('/')
        request.user = self.user
        context = wishlist_count(request)
        self.assertEqual(context['wishlist_count'], 1)

    def test_wishlist_context_processor_anonymous(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        context = wishlist_count(request)
        self.assertEqual(context['wishlist_count'], 0)

    def test_check_wishlist_status_true(self):
        self.client.login(username='testuser', password='testpass')
        Wishlist.objects.create(user=self.user, product=self.product)
        response = self.client.get(reverse('wishlist:check_wishlist_status', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'in_wishlist': True})

    def test_check_wishlist_status_false(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('wishlist:check_wishlist_status', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'in_wishlist': False})

    def test_check_wishlist_status_invalid_product(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('wishlist:check_wishlist_status', args=[999]))
        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(response.content, {'error': 'Product not found'})
