from django.test import TestCase
from django.urls import reverse
from products.models import Product, Category
from decimal import Decimal


class HomeViewTests(TestCase):
    def setUp(self):
        self.categories = {}
        category_names = [
            'cleansers', 'toners', 'serums', 'moisturizers', 'sunscreens'
        ]
        for name in category_names:
            self.categories[name] = Category.objects.create(name=name)

        # Create 3 products per category with increasing ratings
        for cat_key, cat_obj in self.categories.items():
            for rating in [3.5, 4.0, 4.5]:
                Product.objects.create(
                    name=f"{cat_key.capitalize()} Product {rating}",
                    description=(
                        f"Description for {cat_key} product with "
                        f"rating {rating}"
                    ),
                    price=Decimal('10.00'),
                    category=cat_obj,
                    rating=Decimal(str(rating)),
                    sku=f"{cat_key[:3].upper()}{int(rating * 10)}"
                )

    def test_index_view_status_and_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_index_view_featured_products(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        featured_products = response.context['featured_products']

        # Expect one featured product per category (5 total)
        self.assertEqual(len(featured_products), 5)

        for category_name, product in featured_products.items():
            self.assertIsNotNone(
                product,
                f"No featured product returned for category "
                f"'{category_name}'"
            )
            self.assertTrue(product.rating >= 4.5)
            self.assertIn(category_name, self.categories)
            self.assertEqual(
                product.category,
                self.categories[category_name]
            )
