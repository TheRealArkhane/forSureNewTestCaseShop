from django.urls import path

from categories.views import CategoriesDetails, CategoriesView

urlpatterns = [
    path("categories/<int:category_id>/", CategoriesView.as_view()),
    path("categories_products/<int:category_id>/", CategoriesDetails.as_view())
]