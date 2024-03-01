from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import NULLABLE
from users.managers import CustomUserManager


class User(AbstractUser):
    name = models.CharField(max_length=150, default='Anonymous', verbose_name='имя')
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    city = models.CharField(max_length=35, verbose_name='город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)

    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('id',)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    course = models.ForeignKey('materials.Course',
                               on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey('materials.Lesson',
                               on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    sum = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=50,
                                      choices=(('CARD', 'картой'), ('CASH', 'наличными')),
                                      verbose_name='способ оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.course if self.course else self.lesson} - {self.sum}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('user', 'payment_date')
