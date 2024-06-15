from django.urls import path
from .views import UserAccountRegisterAPiView, UserAccountLoginAPiView , UserAccountRefreshAPiView, UserAddDebtAPIView, UserDebtListAPIView, UserDebtUpdateAPIView, UserDebtDeleteAPIView, UserDebtRetrieveAPIView
urlpatterns = [
    path('login/', UserAccountLoginAPiView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', UserAccountRefreshAPiView.as_view(), name='token_refresh'),
    path('register/', UserAccountRegisterAPiView.as_view(), name="register"),
    path('add-debt/', UserAddDebtAPIView.as_view(), name="add_debt"),
    path('list-debts/', UserDebtListAPIView.as_view(), name="debt-list"),
    path('update-debt/<int:pk>/', UserDebtUpdateAPIView.as_view(), name="update_debt"),
    path('delete-debt/<int:pk>/', UserDebtDeleteAPIView.as_view(), name="delete_debt"),
    path('debt-details/<int:pk>/', UserDebtRetrieveAPIView.as_view(), name="debt-details"),
]