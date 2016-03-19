from django.db import models
from django.utils import timezone


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class ToDoItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    task = models.CharField(max_length=200, default='')
    deadline = models.DateTimeField(default=timezone.now)
    isCompleted = models.BooleanField(default=False)

    def post(self):
        self.deadline = timezone.now()
        self.save()

    def __str__(self):
        return self.task


