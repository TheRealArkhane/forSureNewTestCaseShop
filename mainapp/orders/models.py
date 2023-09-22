from django.db import models

from products.models import Product
from users.models import User


class Order(models.Model):
    products = models.ManyToManyField(Product, blank=True, db_constraint=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, db_constraint=False)
    sum = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_quantity = models.IntegerField(default=1)
    address = models.TextField(default='Москва', null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, default='PROCESSING')
