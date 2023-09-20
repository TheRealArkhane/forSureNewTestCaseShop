from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin

from categories.models import Category

admin.site.register(Category, MPTTModelAdmin)

