from django.db import models
from django.core.validators import *

# Create your models here.


class Client(models.Model):
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return "Идентификационный номер пользователя {}".format(
            self.user_id)

    user_id = models.IntegerField(default=0, verbose_name="Идентификационный номер")
    incoming_data = models.DateField(default="", max_length=2048, verbose_name="Дата прохождения теста")
    answer_vector = models.CharField(max_length=32, verbose_name="Вектор ответов",
                                     validators=[validate_comma_separated_integer_list])


class ExtendedClient(models.Model):
    class Meta:
        verbose_name = 'Пользователь с расширенными возможностями'
        verbose_name_plural = 'Пользователи с расширенными возможностями'

    def __str__(self):
        return "Идентификационный номер пользователя с расширенными возможностями {}".format(
            self.user_id)

    user_id = models.IntegerField(default=0, verbose_name="Идентификационный номер")
    incoming_data = models.DateField(default="", max_length=2048, verbose_name="Дата прохождения теста")
    first_name = models.CharField(default="", max_length=256, verbose_name="Имя пользователя")
    second_name = models.CharField(default="", max_length=256, verbose_name="Фамилия пользователя")
    password = models.CharField(default="", max_length=256, verbose_name="Пароль пользователя")
    email = models.EmailField(default="", max_length=256, verbose_name="Почта пользователя")


class Statistic(models.Model):
    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'

    def __str__(self):
        return "Статистика {} - {}".format(
            self.extended_client_user_count,
            self.client_user_count)

    extended_client_user_count = models.IntegerField(default=0, verbose_name="Количество пользователей")
    client_user_count = models.IntegerField(default=0,
                                            verbose_name="Количество пользователей с расширенными возможностями")
