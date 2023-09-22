from django.db import models


class Product(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=100, default='Товар')
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f'id = {self.id}, {self.name}, {self.description}, {self.price}, {self.category_id}'
