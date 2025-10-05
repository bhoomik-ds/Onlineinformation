from django.db import models

# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
