from django.urls import path
from .views import UserAccountRegisterAPiView, UserAccountLoginAPiView , UserAccountRefreshAPiView
urlpatterns = [
    path('login/', UserAccountLoginAPiView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', UserAccountRefreshAPiView.as_view(), name='token_refresh'),
    path('register/', UserAccountRegisterAPiView.as_view(), name="register"),
]