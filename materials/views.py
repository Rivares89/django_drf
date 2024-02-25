from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics

from materials.models import Course, Lesson, Quantity
from materials.serializers import CourseSerializer, LessonSerializer, QuantitySerializer, CourseQuantitySerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

class QuantityCreateAPIView(generics.CreateAPIView):
    serializer_class = QuantitySerializer

class QuantityListAPIView(generics.ListAPIView):
    serializer_class = QuantitySerializer
    queryset = Quantity.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course')
    ordering_fields = ('payment_date')


class CourseQuantityListAPIView(generics.ListAPIView):
    queryset = Quantity.objects.filter(course__isnull=False)
    serializer_class = CourseQuantitySerializer

