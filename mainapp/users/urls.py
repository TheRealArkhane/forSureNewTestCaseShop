from django.urls import path

from users.views import UsersView, UserDetail

urlpatterns = [
    path('users/all', UsersView.as_view()),
    path("users/", UserDetail.as_view()),
]
