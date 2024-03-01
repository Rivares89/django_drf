from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from users import views
from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='пользователи')

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/', views.PaymentListView.as_view(), name='payments'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
