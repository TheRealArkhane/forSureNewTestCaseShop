from django.urls import path

from cart.views import CartDetail, CartSingleEntity

urlpatterns = [
    path("cart/", CartDetail.as_view()),
    path("cart/<int:product_in_cart_id>/", CartSingleEntity.as_view())
]