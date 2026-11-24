from django.urls import path
from users.apps import UsersConfig
from users.views import UserRetrieveUpdateAPIView, PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user-update'),
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
]
