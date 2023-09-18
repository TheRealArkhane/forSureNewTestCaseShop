from django.urls import path

from cart.views import CartDetail, CartView, CartSingleEntity

urlpatterns = [
    path("cart/", CartView.as_view()),
    path("cart/<int:id>/", CartDetail.as_view()),
    path("cart/<int:id>/<int:product_in_cart_id>/", CartSingleEntity.as_view())
]