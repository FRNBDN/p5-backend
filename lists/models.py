from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.id} {self.title}"
