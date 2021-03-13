# Generated by Django 3.1.7 on 2021-03-13 10:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')),
                ('product', models.CharField(choices=[(None, 'Выберите тип продукта'), ('car', 'Авто'), ('consumer', 'Потреб'), ('pledge', 'Залог'), ('mortgage', 'Ипотека')], max_length=20, verbose_name='Продукт')),
                ('phone', models.CharField(help_text='Номер телефона в формате 0000000000', max_length=10, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате 0000000000', regex='^[0-9]{10}$)')], verbose_name='Телефон клиента')),
                ('decision', models.CharField(blank=True, choices=[(None, 'Решение по заявке'), ('approved', 'Одобрено'), ('denied', 'Отказано'), ('temp_denied', 'Временный отказ')], max_length=20, null=True, verbose_name='Решение')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий к решению')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]