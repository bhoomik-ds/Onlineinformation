from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

class Job(models.Model):
    title = models.CharField(max_length=200)
    image = ResizedImageField(
        size=[1200, 800],
        crop=['middle', 'center'],
        upload_to='jobs/',
        quality=85,
        force_format='JPEG',
        null=True,
        blank=True
    )
    short_description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    external_link = models.URLField(max_length=500, verbose_name="External Link", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.pk)])
