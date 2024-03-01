from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User

class Command(BaseCommand):
    help = 'Clear database content'

    def handle(self, *args, **kwargs):
        # Удалить все объекты из всех моделей
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Содержимое базы данных успешно очищено'))
