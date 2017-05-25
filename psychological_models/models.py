from django.db import models
# from development_of_story.models import Answer, Story
from django.core.validators import *

# Create your models here.


class BasisMetric(models.Model):
    class Meta:
        verbose_name = 'Метрика для базисов'
        verbose_name_plural = 'Метрики для базисов'

    def __str__(self):
        return "{}".format(self.name)

    name = models.CharField(default="Новая метрика", max_length=256, verbose_name="Название метрики")


class BasisOfPsychotype(models.Model):
    class Meta:
        verbose_name = 'Базис психотипов'
        verbose_name_plural = 'Базисы психотипов'

    def __str__(self):
        return "{}".format(self.name)

    name = models.CharField(default="Новый базис", max_length=256, verbose_name="Название базиса психотипов")
    description = models.TextField(default="", max_length=2048, verbose_name="Описание базиса психотипов.")
    metric = models.ForeignKey(BasisMetric, verbose_name="Метрика")
    symptom_count = models.IntegerField(default=0, verbose_name="Число признаков", help_text="Длина булевого вектора.")
    # symptom_names = models.CharField(max_length=256, verbose_name="Затычка масива названий признаков")      # debug
    parameter_count = models.IntegerField(default=0, verbose_name="Число параметров", help_text="Длина вектора чисел.")
    # parameter_names = models.CharField(max_length=256, verbose_name="Затычка масива названий параметров")     # debug
    # story = models.ManyToManyField(Story)


