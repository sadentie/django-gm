from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Goals(models.Model):
    goal = models.CharField('Цель', max_length=250)
    datestart = models.DateField('Дата начала цели', default=date.today())
    dateend = models.DateField('Дата конца цели',default=None, null=True, blank=True)
    username = models.CharField('Пользователь', max_length=250, default=None)
    
    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return self.goal
    
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'


class CompletedGoals(models.Model):
    goal = models.CharField('Цель', max_length=250)
    timespend = models.IntegerField('Времени потрачено')
    enddate = models.DateField('Дата окончания')
    user = models.CharField('Пользователь', max_length=250, default=None)

    def __str__(self):
        return self.goal

    class Meta:
        verbose_name = 'Законченная цель'
        verbose_name_plural = 'Законченные цели'


class CanseledGoals(models.Model):
    goal = models.CharField('Цель', max_length=250)
    timespend = models.IntegerField('Времени потрачено')

    def __str__(self):
        return self.goal
    
    class Meta:
        verbose_name = 'Отмененная цель'
        verbose_name_plural = 'Отмененные цели'