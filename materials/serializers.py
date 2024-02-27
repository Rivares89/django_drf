from rest_framework import serializers
from materials.models import Course, Lesson, Quantity

class QuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Quantity
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    course_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_course_quantity(self, instance):
        quantity_instance = instance.quantity_set.first()
        if quantity_instance:
            return quantity_instance.quantity
        return 0

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseQuantitySerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Quantity
        fields = ('quantity', 'course')
