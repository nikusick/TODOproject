from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Task(models.Model):
    name = models.CharField(max_length=150)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
