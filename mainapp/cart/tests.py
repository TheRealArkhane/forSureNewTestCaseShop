from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate

from cart.views import CartDetail
from products.models import Product
from users.models import User


class TestCart(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(
            name='test_product',
            price='100',
            description='test'
        )
        self.admin = User.objects.create_superuser('testadm', 'admin@test.ru', '1234')

    def test_cart_create(self):
        factory = APIRequestFactory()
        request = factory.post('/cart/', {
            'products': self.product.id,
            'quantity': 2,
            'price': 300,
            'user_id': self.admin.id},
            format='json')
        force_authenticate(request, self.admin)
        view = CartDetail.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
