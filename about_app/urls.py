
from django.urls import path
from .views import AboutListView
urlpatterns = [
    path('list/', AboutListView.as_view(), name='about-list'),

]
