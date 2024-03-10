from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from materials.models import Course, Lesson, Quantity, Subscription
from materials.paginators import LessonPaginator
from materials.permissions import IsOwnerOrStaff, IsManager, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer, QuantitySerializer, CourseQuantitySerializer

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny] # [IsAuthenticated, ~IsManager]
        elif self.action == 'list':
            self.permission_classes = [AllowAny] # [IsAuthenticated, IsOwner | IsManager]

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
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated, ~IsManager]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsManager | IsOwner]
    pagination_class = LessonPaginator

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsManager | IsOwner]

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsManager | IsOwner]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    # permission_classes = [IsOwnerOrStaff, IsOwner]

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

class SubscribeAPIView(APIView):

    def post(self, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item, created = Subscription.objects.get_or_create(user=user, course=course_item)

        if created:
            message = 'Вы подписались на обновления курса'
        else:
            subs_item.delete()
            message = 'Вы отписались от обновления курса'

        return Response({"message": message})
