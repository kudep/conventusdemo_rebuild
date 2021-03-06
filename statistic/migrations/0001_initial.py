# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 18:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='Идентификационный номер')),
                ('incoming_data', models.DateField(default='', max_length=2048, verbose_name='Дата прохождения теста')),
                ('answer_vector', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Вектор ответов')),
            ],
            options={
                'verbose_name_plural': 'Клиенты',
                'verbose_name': 'Клиент',
            },
        ),
        migrations.CreateModel(
            name='ExtendedClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='Идентификационный номер')),
                ('incoming_data', models.DateField(default='', max_length=2048, verbose_name='Дата прохождения теста')),
                ('first_name', models.CharField(default='', max_length=256, verbose_name='Имя пользователя')),
                ('second_name', models.CharField(default='', max_length=256, verbose_name='Фамилия пользователя')),
                ('password', models.CharField(default='', max_length=256, verbose_name='Пароль пользователя')),
                ('email', models.EmailField(default='', max_length=256, verbose_name='Почта пользователя')),
            ],
            options={
                'verbose_name_plural': 'Пользователи с расширенными возможностями',
                'verbose_name': 'Пользователь с расширенными возможностями',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_client_user_count', models.IntegerField(default=0, verbose_name='Количество пользователей')),
                ('client_user_count', models.IntegerField(default=0, verbose_name='Количество пользователей с расширенными возможностями')),
            ],
            options={
                'verbose_name_plural': 'Статистики',
                'verbose_name': 'Статистика',
            },
        ),
    ]
