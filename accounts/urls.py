from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)


urlpatterns = [
    path('login', CustomTokenObtainPairView.as_view()),
    path('refresh', CustomTokenRefreshView.as_view()),
    path('verify', CustomTokenVerifyView.as_view()),
    path('logout', LogoutView.as_view()),
]
