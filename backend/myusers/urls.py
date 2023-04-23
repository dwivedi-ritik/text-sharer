from django.urls import path
import myusers.views as views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('token', TokenObtainPairView.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register', views.signup),
]
