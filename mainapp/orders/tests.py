from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from cart.models import Cart
from orders.views import OrderView
from products.models import Product
from users.models import User


class TestOrder(TestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(
            name='test_product',
            price='100',
            description='test'
        )
        self.admin = User.objects.create_superuser('testadm', 'admin@test.ru', '1234')
        self.cart = Cart.objects.create(
            products=self.product,
            quantity=2,
            user_id=self.admin.id
        )

    def test_order_create(self):
        factory = APIRequestFactory()
        request = factory.post('/orders/',
                               {
                                   'address': 'test'
                               }, format='json')
        force_authenticate(request, self.admin)
        view = OrderView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
