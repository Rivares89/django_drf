from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class MaterialsTestCase(APITestCase):

    def setUp(self) -> None:

        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False,
        )
        self.user.set_password("test_user")
        self.user.save()

        self.course = Course.objects.create(
            title="Test_course",
            description="Test_course",
            # owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson'
            # owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_list_lessons(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('materials:lesson-list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        # self.assertEquals(
        #     response.json(),
        #     {
        #         'count': 1,
        #         'next': None,
        #         'previous': None,
        #         'results': [
        #             {
        #                 'id': self.lesson.id,
        #                 'title': self.lesson.title,
        #                 'preview': self.lesson.preview,
        #                 'description': self.lesson.description,
        #                 'video_link': self.lesson.video_link,
        #                 'course': self.lesson.course,
        #                 'owner': self.user.id
        #             }
        #         ]
        #     }
        # )
###########################
    # def test_create_course(self):
    #         """Тестирование создания курса"""
    #         data = {
    #             'title': 'Test',
    #             'description': 'Test',
    #         }
    #         response = self.client.post(
    #             '/courses/',
    #             data=data
    #         )
    #
    #         self.assertEqual(
    #             response.status_code,
    #             status.HTTP_201_CREATED
    #         )
    #
    #         self.assertEqual(
    #             response.json(),
    #             {'id': 1, 'course_quantity': 0, 'title': 'Test', 'preview': None, 'description': 'Test', 'owner': None}
    #
    #         )
    #
    #         self.assertTrue(
    #             Course.objects.all().exists()
    #         )
    #
    # def test_list_course(self):
    #     """Тестирование списка курсов"""
    #
    #     Course.objects.create(
    #         title='list_test',
    #         description='list_test'
    #     )
    #
    #     response = self.client.get(
    #         '/courses/'
    #     )
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #
    #     self.assertEqual(
    #         response.json(),
    #         [{'id': 2, 'course_quantity': 0, 'title': 'list_test', 'preview': None, 'description': 'list_test', 'owner': None}
# ]
#         )


