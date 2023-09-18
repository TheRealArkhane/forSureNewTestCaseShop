from django.urls import path

from products.views import ProductsView, ProductDetail

urlpatterns = [
    path('products/', ProductsView.as_view()),
    path("products/<int:id>/", ProductDetail.as_view()),
]
