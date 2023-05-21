from django.db import models
from django.utils.timezone import now


class Task(models.Model):
    name = models.TextField()
    details = models.TextField()
    start_day = models.DateField(default=now)
    stop_day = models.DateField()
