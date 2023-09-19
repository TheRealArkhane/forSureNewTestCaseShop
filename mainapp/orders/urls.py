from django.urls import path

from orders.views import OrderView

urlpatterns = [
    path("orders/<int:id>/", OrderView.as_view())
]
