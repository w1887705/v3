from django.conf import settings
from django.db import models

class Task(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.order}. {self.title}"

class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    last_score = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "task")

class Attempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    notes = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
