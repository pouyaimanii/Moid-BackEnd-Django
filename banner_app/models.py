from django.db import models

class BannerModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='banner_videos/', null=True, blank=True)

    def __str__(self):
        return self.title