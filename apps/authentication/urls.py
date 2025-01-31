from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.views import LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]