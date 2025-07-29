from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Category
from decimal import Decimal

class BagViewsTest(TestCase):
    def setUp(self):
        # Create a Category instance (required for Product)
        self.category = Category.objects.create(
            name="Test Category"
        )
        # Create a Product instance with the required category
        self.product = Product.objects.create(
            name="Test Product",
            description="Test product description",
            price=Decimal('10.00'),
            category=self.category,  # assign the created category here
            sku="TESTSKU123"
            # rating, image_url, image are optional and can be omitted
        )
        self.client = Client()

    def test_view_bag_get(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag_new_item(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.pk]),
            {'quantity': 2, 'redirect_url': reverse('view_bag')},
            follow=True
        )
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        bag = session.get('bag', {})
        self.assertIn(str(self.product.pk), bag)
        self.assertEqual(bag[str(self.product.pk)], 2)

    def test_add_to_bag_existing_item(self):
        # Add first
        session = self.client.session
        session['bag'] = {str(self.product.pk): 1}
        session.save()

        # Add again
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.pk]),
            {'quantity': 3, 'redirect_url': reverse('view_bag')},
            follow=True
        )
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        bag = session.get('bag', {})
        self.assertEqual(bag[str(self.product.pk)], 4)  # 1 + 3

    def test_adjust_bag_increase_quantity(self):
        session = self.client.session
        session['bag'] = {str(self.product.pk): 1}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.product.pk]),
            {'quantity': 5},
            follow=True
        )
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        bag = session.get('bag', {})
        self.assertEqual(bag[str(self.product.pk)], 5)

    def test_adjust_bag_remove_item(self):
        session = self.client.session
        session['bag'] = {str(self.product.pk): 1}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.product.pk]),
            {'quantity': 0},
            follow=True
        )
        self.assertRedirects(response, reverse('view_bag'))
        session = self.client.session
        bag = session.get('bag', {})
        self.assertNotIn(str(self.product.pk), bag)

    def test_remove_from_bag_success(self):
        session = self.client.session
        session['bag'] = {str(self.product.pk): 1}
        session.save()

        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.pk])
        )
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        bag = session.get('bag', {})
        self.assertNotIn(str(self.product.pk), bag)

    def test_remove_from_bag_product_not_found(self):
        # This will raise 404 because product 999 does not exist
        response = self.client.post(
            reverse('remove_from_bag', args=[999])
        )
        self.assertEqual(response.status_code, 404)
