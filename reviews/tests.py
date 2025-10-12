from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Category
from .models import Review
from .forms import ReviewForm


class ReviewFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        self.category = Category.objects.create(name='Test Category')

        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            category=self.category
        )

    def test_review_form_valid_data(self):
        """
        Test that the review form accepts valid data
        """
        form_data = {
            'rating': 5,
            'comment': 'Great product!'
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid_rating(self):
        """
        Test that the review form rejects invalid ratings
        """
        form_data = {
            'rating': 0,
            'comment': 'Great product!'
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

        form_data = {
            'rating': 6,
            'comment': 'Great product!'
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

    def test_review_form_empty_comment(self):
        """
        Test that the review form requires a comment
        """
        form_data = {
            'rating': 5,
            'comment': ''
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors)

    def test_review_form_widget_attributes(self):
        """
        Test that the star rating widget has correct attributes
        """
        form = ReviewForm()
        rating_field = form.fields['rating']
        self.assertEqual(rating_field.min_value, 1)
        self.assertEqual(rating_field.max_value, 5)
        self.assertIsInstance(
            rating_field.widget,
            type(ReviewForm().fields['rating'].widget)
        )


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        self.category = Category.objects.create(name='Test Category')

        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            category=self.category
        )

    def test_review_creation(self):
        """
        Test that a review can be created
        """
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
        """
        Test the string representation of a review
        """
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment='Great product!'
        )
        expected_string = (
            f"Review by {self.user.username} on {self.product.name}"
        )
        self.assertEqual(str(review), expected_string)


class ProductRatingTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='testpass123'
        )
        self.user3 = User.objects.create_user(
            username='user3',
            email='user3@example.com',
            password='testpass123'
        )

        self.category = Category.objects.create(name='Test Category')

        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            category=self.category
        )

    def test_product_average_rating_calculation(self):
        """
        Test that product average rating is calculated correctly
        """
        # Initially no reviews
        self.assertIsNone(self.product.get_average_rating())
        self.assertEqual(self.product.get_review_count(), 0)
        self.assertEqual(self.product.get_rating_display(), "No reviews yet")

        # Add first review
        Review.objects.create(
            product=self.product,
            user=self.user1,
            rating=5,
            comment='Excellent!'
        )
        self.product.refresh_from_db()
        self.assertEqual(self.product.get_average_rating(), 5.0)
        self.assertEqual(self.product.get_review_count(), 1)
        self.assertEqual(self.product.get_rating_display(), "5.0/5 (1 review)")

        # Add second review
        Review.objects.create(
            product=self.product,
            user=self.user2,
            rating=3,
            comment='Good product'
        )
        self.product.refresh_from_db()
        self.assertEqual(self.product.get_average_rating(), 4.0)
        self.assertEqual(self.product.get_review_count(), 2)
        self.assertEqual(self.product.get_rating_display(), "4.0/5 (2 reviews)")

        # Add third review
        Review.objects.create(
            product=self.product,
            user=self.user3,
            rating=4,
            comment='Pretty good'
        )
        self.product.refresh_from_db()
        self.assertEqual(self.product.get_average_rating(), 4.0)
        self.assertEqual(self.product.get_review_count(), 3)
        self.assertEqual(self.product.get_rating_display(), "4.0/5 (3 reviews)")

    def test_product_rating_signals(self):
        """
        Test that product rating is automatically updated when reviews change
        """
        # Initially no rating
        self.assertIsNone(self.product.rating)

        # Add a review - should trigger signal
        review = Review.objects.create(
            product=self.product,
            user=self.user1,
            rating=5,
            comment='Great!'
        )
        self.product.refresh_from_db()
        self.assertEqual(self.product.rating, 5.0)

        # Update the review - should trigger signal
        review.rating = 3
        review.save()
        self.product.refresh_from_db()
        self.assertEqual(self.product.rating, 3.0)

        # Delete the review - should trigger signal
        review.delete()
        self.product.refresh_from_db()
        self.assertIsNone(self.product.rating)