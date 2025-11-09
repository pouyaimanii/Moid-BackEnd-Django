from django.db import models

class NewsletterModel(models.Model):
    email = models.EmailField()
    birth_year = models.IntegerField(null=True, blank=True)
    birth_month = models.IntegerField(null=True, blank=True)
    birth_day = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.email
    