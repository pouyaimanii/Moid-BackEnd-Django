
from django.urls import path
from .views import MovieListView
urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie-list'),
]