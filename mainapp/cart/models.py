from _pydecimal import Decimal

from django.db import models

from django.db import models
from products.models import Product
from users.models import User


class Cart(models.Model):
    products = models.ForeignKey(Product, related_name="carts", blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", blank=True)
