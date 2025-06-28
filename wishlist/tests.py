from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Category, Product
from .models import Wishlist


class WishlistTestCase(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=19.99,
            category=self.category
        )

    def test_add_to_wishlist(self):
        """Test adding a product to wishlist"""
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.post(
            reverse('wishlist:add_to_wishlist', args=[self.product.id])
        )
        
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertTrue(Wishlist.objects.filter(
            user=self.user, 
            product=self.product
        ).exists())

    def test_remove_from_wishlist(self):
        """Test removing a product from wishlist"""
        self.client.login(username='testuser', password='testpass123')
        
        # First add to wishlist
        wishlist_item = Wishlist.objects.create(
            user=self.user,
            product=self.product
        )
        
        response = self.client.post(
            reverse('wishlist:remove_from_wishlist', args=[self.product.id])
        )
        
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertFalse(Wishlist.objects.filter(
            user=self.user, 
            product=self.product
        ).exists())

    def test_wishlist_view_requires_login(self):
        """Test that wishlist view requires authentication"""
        response = self.client.get(reverse('wishlist:wishlist'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_wishlist_view_authenticated(self):
        """Test wishlist view for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.get(reverse('wishlist:wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_duplicate_wishlist_item(self):
        """Test that duplicate wishlist items are not created"""
        self.client.login(username='testuser', password='testpass123')
        
        # Add first time
        self.client.post(reverse('wishlist:add_to_wishlist', args=[self.product.id]))
        
        # Try to add again
        self.client.post(reverse('wishlist:add_to_wishlist', args=[self.product.id]))
        
        # Should only have one item
        self.assertEqual(Wishlist.objects.filter(
            user=self.user, 
            product=self.product
        ).count(), 1) 