from django.db import models




class AboutModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about_image/', blank=True, null=True)

    def __str__(self):
        return self.title
