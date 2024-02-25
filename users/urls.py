from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
]