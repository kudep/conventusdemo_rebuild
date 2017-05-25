from django.db import models
from statistic.models import Client
from psychological_models.models import BasisOfPsychotype
from django.core.validators import *

# Create your models here.


class Story(models.Model):
    class Meta:
        verbose_name = 'Сюжет'
        verbose_name_plural = 'Сюжеты'

    def __str__(self):
        return "{}".format(
            self.title)

    title = models.CharField(default="Новая история", max_length=256, verbose_name="Название сюжета")
    description = models.TextField(default="", max_length=2048, verbose_name="Описание сюжета")
    likes = models.IntegerField(default=0, verbose_name="Нравится")
    bases = models.ManyToManyField(BasisOfPsychotype, verbose_name="Базисы", help_text="Выберите хотя бы один базис")


class Scene(models.Model):
    class Meta:
        verbose_name = 'Сцена'
        verbose_name_plural = 'Сцены'

    def __str__(self):
        return "{}".format(
            self.title)

    title = models.CharField(default="Новая сцена", max_length=256, verbose_name="Название сцены")
    description = models.TextField(default="", max_length=2048, verbose_name="Описание сцены.")
    question = models.TextField(default="?", max_length=1024, verbose_name="Вопрос")
    likes = models.IntegerField(default=0, verbose_name="Нравится")

    story = models.ForeignKey(Story, verbose_name="Из истории")
    scene_order = models.PositiveSmallIntegerField(default=0, verbose_name="Порядок в истории")


class Answer(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return "{} - {} - {}".format(self.story.title, self.scene.title, self.answer)

    story = models.ForeignKey(Story, verbose_name="Из истории")
    scene = models.ForeignKey(Scene, verbose_name="Из сцены")
    answer = models.CharField(default="", max_length=1024, verbose_name="Ответ")
    # characteristic = models.OneToOneField(PsychotypeCharacteristic,
    #                                       verbose_name="Характеристика ответа в базисе психотипа")


class PsychotypeCharacteristic(models.Model):
    class Meta:
        verbose_name = 'Характеристика психотипа'
        verbose_name_plural = 'Характеристики психотипа'

    def __str__(self):
        return "Характеристика на основе  {}, вектор признаков = [{}], вектор параметров = [{}]".format(
            self.basis,
            self.symptom_vector,
            self.parameter_vector)

    answer = models.ForeignKey(Answer, verbose_name="Характеризует вопрос")
    basis = models.ForeignKey(BasisOfPsychotype, verbose_name="На основе базиса")
    symptom_vector = models.CharField(max_length=32, verbose_name="Вектор признаков", validators=[validate_comma_separated_integer_list], default='0,0,0,0,0,0,0,0,0,0,0')
    parameter_vector = models.CharField(max_length=32, verbose_name="Вектор параметров",
                                        validators=[validate_comma_separated_integer_list], default='0,0,0,0,0,0,0,0,0,0,0')


class ClientAndAnswerConnection(models.Model):
    class Meta:
        verbose_name = 'Связь клиента и ответа'
        verbose_name_plural = 'Связи клиентов и ответов'

    def __str__(self):
        return "{} to {}".format(self.client, self.answer)

    client = models.ForeignKey(Client, verbose_name="Привязка к клиенту")
    answer = models.ForeignKey(Answer, verbose_name="Привязка к ответу")
