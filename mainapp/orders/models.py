from django.db import models

import users.models
from products.models import Product
from users.models import User


class Order(models.Model):
    products = models.ManyToManyField(Product, blank=True, db_constraint=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, db_constraint=False)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, default='PROCESSING')
