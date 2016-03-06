from django.db import models
from django.utils import timezone

# Create your models here.
class toDoItem(models.Model):
    task = models.CharField(max_length=200, default='')
    deadline = models.DateTimeField(default=timezone.now)
    isCompleted = models.BooleanField(default="false")

    def post(self):
        self.deadline = timezone.now()
        self.save()

    def __str__(self):
        return self.task
