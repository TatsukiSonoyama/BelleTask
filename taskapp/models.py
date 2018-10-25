from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    limit_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title
