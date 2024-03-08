from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson, Quantity
from materials.permissions import IsOwnerOrStaff, IsManager, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer, QuantitySerializer, CourseQuantitySerializer

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsManager]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsOwner | IsManager]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsOwner | IsManager]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsOwner | IsManager]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsManager | IsOwner]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsManager | IsOwner]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsManager | IsOwner]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff, IsOwner]

class QuantityCreateAPIView(generics.CreateAPIView):
    serializer_class = QuantitySerializer
    permission_classes = [IsAuthenticated, IsManager | IsOwner]

class QuantityListAPIView(generics.ListAPIView):
    serializer_class = QuantitySerializer
    queryset = Quantity.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course',)
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated, IsManager | IsOwner]

class CourseQuantityListAPIView(generics.ListAPIView):
    queryset = Quantity.objects.filter(course__isnull=False)
    serializer_class = CourseQuantitySerializer
    permission_classes = [IsAuthenticated, IsManager | IsOwner]
