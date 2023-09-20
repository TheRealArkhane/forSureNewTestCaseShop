from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from products.models import Product


class Category(MPTTModel):
    id = models.BigAutoField
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    products = models.ManyToManyField(Product, blank=True, db_constraint=False)

    def __str__(self):
        return f'id = {self.id}, {self.name}, {self.parent}'

    class MPTTMeta:
        order_insertion_by = ['id']

