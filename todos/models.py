from django.db import models
import datetime, uuid
from django.utils import timezone


class ToDo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    task = models.TextField()
    created_time = models.DateField(default=timezone.now)
    finished_time = models.DateTimeField(null=True, blank=True)


