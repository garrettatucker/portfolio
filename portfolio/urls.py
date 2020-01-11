from . import views
from django.urls import path, include
from django.conf import settings

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='home'),
]