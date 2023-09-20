import logging

from django.test import TestCase
from categories.models import Category

# Create your tests here.
logger = logging.getLogger()
logger.level = logging.INFO


class TestMPTT(TestCase):

    def test_hierarchy(self):
        root = Category.objects.create(name="Root")
        clothes = Category.objects.create(name="Clothes", parent=root)
        man_clothes = Category.objects.create(name="Mans Clothes", parent=clothes)
        coats = Category.objects.create(name="Coats", parent=man_clothes)

        logger.info("Root descendants")
        logger.info(root.get_descendants())

        assert root.get_descendants()
