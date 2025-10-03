from django.db import models

class MovieModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='television_image/', blank=True, null=True)

    def __str__(self):
        return self.title
