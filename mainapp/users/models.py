from django.db import models


class User(models.Model):
    id = models.BigAutoField
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    email = models.EmailField(default='test@test.ru', max_length=255)
    encrypted_password = models.CharField(default='1234', max_length=255)

    def __str__(self):
        return self.first_name, self.last_name
