from django.db import models

import users.models
from products.models import Product
from users.models import User


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name="orders", blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_orders", blank=True)
    order_date = models.DateField(default='2023-09-19')
    status = models.CharField(max_length=32, default='PROCESSING')
