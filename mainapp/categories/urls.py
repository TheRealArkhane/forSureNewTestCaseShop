from django.urls import path

from categories.views import CategoriesDetails, CategoriesView

urlpatterns = [
    path("categories/<int:id>/", CategoriesView.as_view()),
    path("categories_products/<int:id>/", CategoriesDetails.as_view())
]