from django.db import models
from django.core import validators
from concurrency.fields import IntegerVersionField


class Application(models.Model):
    class Product(models.TextChoices):
        CAR = 'car', 'Авто'
        CONSUMER = 'consumer', 'Потреб'
        PLEDGE = 'pledge', 'Залог'
        MORTGAGE = 'mortgage', 'Ипотека'
        __empty__ = 'Выберите тип продукта'

    class Decision(models.TextChoices):
        APPROVED = 'approved', 'Одобрено'
        DENIED = 'denied', 'Отказано'
        TEMPORARILY_DENIED = 'temp_denied', 'Временный отказ'
        __empty__ = 'Решение по заявке'

    date = models.DateTimeField('Дата заявки', auto_now_add=True)
    product = models.CharField('Продукт', choices=Product.choices, max_length=20)
    phone = models.CharField(
        'Телефон клиента',
        validators=[validators.RegexValidator(
            regex='^[0-9]{10}$',
            message='Номер телефона должен быть в формате 0000000000'
        )],
        max_length=10,
        help_text='Номер телефона в формате 0000000000'
    )
    decision = models.CharField('Решение', choices=Decision.choices, max_length=20, blank=True, null=True)
    comment = models.TextField('Комментарий к решению', blank=True, null=True)
    version = IntegerVersionField()     # реализация конкурентности

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.phone} - {self.product}'


class AppLogs(models.Model):
    class Product(models.TextChoices):
        CAR = 'car', 'Авто'
        CONSUMER = 'consumer', 'Потреб'
        PLEDGE = 'pledge', 'Залог'
        MORTGAGE = 'mortgage', 'Ипотека'
        __empty__ = 'Выберите тип продукта'

    class Decision(models.TextChoices):
        APPROVED = 'approved', 'Одобрено'
        DENIED = 'denied', 'Отказано'
        TEMPORARILY_DENIED = 'temp_denied', 'Временный отказ'
        __empty__ = 'Решение по заявке'

    app_id = models.IntegerField('ID заявки')
    date = models.DateTimeField('Дата изменения заявки', auto_now_add=True)
    product = models.CharField('Продукт', choices=Product.choices, max_length=20)
    phone = models.CharField(
        'Телефон клиента',
        validators=[validators.RegexValidator(
            regex='^[0-9]{10}$',
            message='Номер телефона должен быть в формате 0000000000'
        )],
        max_length=10,
        help_text='Номер телефона в формате 0000000000'
    )
    decision = models.CharField('Решение', choices=Decision.choices, max_length=20, blank=True, null=True)
    comment = models.TextField('Комментарий к решению', blank=True, null=True)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        return f'{self.phone} - {self.product}'
