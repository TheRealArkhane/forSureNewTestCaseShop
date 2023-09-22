from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status
from users.models import User
from products.models import Product
from products.views import ProductsView, ProductDetail


class TestProductViewSet(TestCase):

    def setUp(self) -> None:
        self.product = Product.objects.create(
            name='test_product',
            price='100',
            description='test'
        )
        self.admin = User.objects.create_superuser('testadm', 'admin@test.ru', '1234')

    def test_get_products(self):
        factory = APIRequestFactory()
        request = factory.get('/products/')
        view = ProductsView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


