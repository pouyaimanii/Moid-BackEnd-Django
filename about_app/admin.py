from django.contrib import admin
from .models import AboutModel

@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    list_display=['title',]