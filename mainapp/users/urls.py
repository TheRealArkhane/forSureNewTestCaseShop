from django.urls import path

from users.views import UsersView, UserDetail

urlpatterns = [
    path('users/', UsersView.as_view()),
    path("users/<int:id>/", UserDetail.as_view()),
]
