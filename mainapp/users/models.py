from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField(default='2000-01-01')

    def __str__(self):
        return (f'id = '
                f'{self.id},'
                f' {self.first_name} {self.last_name}, {self.birth_date}, is superuser = {self.is_superuser}')
