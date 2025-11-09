from rest_framework import serializers
from .models import NewsletterModel




class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterModel
        fields = ['id', 'email', 'birth_year', 'birth_month', 'birth_day']

