
from django.urls import path
from .views import NewsletterView
urlpatterns = [
    path('create/', NewsletterView.as_view(), name='newsletter'),

]
