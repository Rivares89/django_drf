from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, QuantityCreateAPIView, CourseQuantityListAPIView, QuantityListAPIView, \
    SubscribeAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('quantity/', QuantityListAPIView.as_view(), name='quantity-list'),
    path('quantity/create/', QuantityCreateAPIView.as_view(), name='quantity-create'),
    path('course/quantity/', CourseQuantityListAPIView.as_view(), name='course-quantity'),
    path('subscription/', SubscribeAPIView.as_view(), name='subscribe'),
] + router.urls
