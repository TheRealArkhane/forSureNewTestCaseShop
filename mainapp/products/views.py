from django.shortcuts import render
from .serializers import ProductsSerializer
from .models import Product
from rest_framework import generics


class ProductView(generics.ListAPIView):
    serializer_class = ProductsSerializer
