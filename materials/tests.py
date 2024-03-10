from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson, Subscription
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

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.lesson.id,
                        'title': self.lesson.title,
                        'description': self.lesson.description,
                        'preview': self.lesson.preview,
                        'video_link': self.lesson.video_link,
                        'course': self.lesson.course
                    }
                ]
            }
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""

        data = {
            "title": "test_lesson2",
            "description": "test_lesson2",
            "course": 1
        }

        response = self.client.post(
            reverse('materials:lesson-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json()['title'],
            data['title']
        )

    def test_update_lesson(self):
        """Тестирование изменения информации об уроке"""
        lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson'
        )

        response = self.client.patch(
            f'/lesson/update/{lesson.id}/',
            {'description': 'change'},
            format='json'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        lesson = Lesson.objects.create(
            title='Test_lesson',
            description='Test_lesson'
        )

        response = self.client.delete(
            f'/lesson/delete/{lesson.id}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    class SubscriptionTestCase(APITestCase):

        def setUp(self):
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
                owner=self.user
            )

            self.client.force_authenticate(user=self.user)

        def test_subscribe_to_course(self):
            """Тест на создание подписки на курс"""

            data = {
                "user": self.user.id,
                "course": self.course.id,
            }

            response = self.client.post(
                reverse('materials:subscribe'),
                data=data
            )
            print(response.json())

            self.assertEquals(
                response.status_code,
                status.HTTP_201_CREATED
            )

            self.assertEquals(
                response.json(),
                {'message': 'Вы подписались на обновления курса'}
            )


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


