from django.db import models


class Product(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name, self.description, self.price
