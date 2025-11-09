from django.contrib import admin
from .models import NewsletterModel

@admin.register(NewsletterModel)
class NewsletterAdmin(admin.ModelAdmin):
    list_display=['email',]