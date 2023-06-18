from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Task(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    details = models.TextField(verbose_name='Детали')
    start_day = models.DateField(default=now, verbose_name='Начало')
    stop_day = models.DateField(verbose_name='Окончание')
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
