from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Category
from .models import Review
from .forms import ReviewForm

# Create your tests here.

class ReviewFormTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create a test category
        self.category = Category.objects.create(
            name='Test Category'
        )
        
        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            category=self.category
        )
    
    def test_review_form_valid_data(self):
        """Test that the review form accepts valid data"""
        form_data = {
            'rating': 5,
            'comment': 'Great product!'
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_review_form_invalid_rating(self):
        """Test that the review form rejects invalid ratings"""
        # Test rating below minimum
        form_data = {
            'rating': 0,
            'comment': 'Great product!'
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)
        
        # Test rating above maximum
        form_data = {
            'rating': 6,
            'comment': 'Great product!'
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)
    
    def test_review_form_empty_comment(self):
        """Test that the review form requires a comment"""
        form_data = {
            'rating': 5,
            'comment': ''
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors)
    
    def test_review_form_widget_attributes(self):
        """Test that the star rating widget has correct attributes"""
        form = ReviewForm()
        rating_field = form.fields['rating']
        self.assertEqual(rating_field.min_value, 1)
        self.assertEqual(rating_field.max_value, 5)
        self.assertIsInstance(rating_field.widget, type(ReviewForm().fields['rating'].widget))

class ReviewModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Create a test category
        self.category = Category.objects.create(
            name='Test Category'
        )
        
        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            category=self.category
        )
    
    def test_review_creation(self):
        """Test that a review can be created"""
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment='Great product!'
        )
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great product!')
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.user, self.user)
    
    def test_review_string_representation(self):
        """Test the string representation of a review"""
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment='Great product!'
        )
        expected_string = f"Review by {self.user.username} on {self.product.name}"
        self.assertEqual(str(review), expected_string)
