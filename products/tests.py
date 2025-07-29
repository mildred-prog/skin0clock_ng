from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import Category, Product
from .forms import ProductForm
from . import views


class ProductAppTests(TestCase):

    def setUp(self):
        self.client = Client()

        # Create category and product
        self.category = Category.objects.create(name='Serums')
        self.product = Product.objects.create(
            name='Glow Serum',
            sku='GS001',
            description='Brightens and evens skin tone.',
            price=29.99,
            category=self.category
        )

        # Create superuser for admin views
        self.superuser = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='adminpass'
        )

        # Create regular user
        self.user = User.objects.create_user(
            username='user', email='user@example.com', password='userpass'
        )

    # ---------- MODELS ----------

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Serums')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Glow Serum')

    def test_product_category_relation(self):
        self.assertEqual(self.product.category.name, 'Serums')

    # ---------- FORMS ----------

    def test_product_form_valid(self):
        form = ProductForm(data={
            'name': 'Night Cream',
            'sku': 'NC001',
            'description': 'Hydrating night cream',
            'price': 18.99,
            'category': self.category.id
        })
        self.assertTrue(form.is_valid())

    def test_product_form_invalid_missing_name(self):
        form = ProductForm(data={
            'sku': 'NC002',
            'description': 'Missing name',
            'price': 10.00,
            'category': self.category.id
        })
        self.assertFalse(form.is_valid())

    # ---------- VIEWS ----------

    def test_all_products_view(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_view(self):
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Glow Serum')

    def test_add_product_view_superuser(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_edit_product_view_superuser(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_delete_product_view_superuser(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('delete_product', args=[self.product.id]))
        self.assertRedirects(response, reverse('products'))
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

    def test_add_product_view_restricted_for_non_superuser(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    # ---------- URL RESOLUTION ----------

    def test_url_all_products(self):
        self.assertEqual(resolve(reverse('products')).func, views.all_products)

    def test_url_product_detail(self):
        resolved_func = resolve(reverse('product_detail', args=[self.product.id])).func
        self.assertEqual(resolved_func, views.product_detail)

    def test_url_add_product(self):
        self.assertEqual(resolve(reverse('add_product')).func, views.add_product)

    def test_url_edit_product(self):
        self.assertEqual(resolve(reverse('edit_product', args=[self.product.id])).func, views.edit_product)

    def test_url_delete_product(self):
        self.assertEqual(resolve(reverse('delete_product', args=[self.product.id])).func, views.delete_product)
