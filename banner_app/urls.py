
from django.urls import path
from .views import BannerListView
urlpatterns = [
    path('list/', BannerListView.as_view(), name='banner-list'),

]
