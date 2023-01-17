from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from lists.models import List
from datetime import datetime


def tomorrow():
    return timezone.now() + timedelta(days=1)


class Item(models.Model):
    priority_choice = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    state_choice = [
        ('todo', 'To-do'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    due_date = models.DateField(default=tomorrow)
    overdue = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=priority_choice,
        default='medium'
        )
    state = models.CharField(
        max_length=10,
        choices=state_choice,
        default='todo'
        )
    file = models.ImageField(
        upload_to='raw/',
        blank=True,
        storage=RawMediaCloudinaryStorage()
        )

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return f"{self.title} {self.description}"