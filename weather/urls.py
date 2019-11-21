from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='weather'), #the path for our index view
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
]