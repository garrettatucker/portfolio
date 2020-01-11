from django.conf.urls import include, url
from . import views

app_name = 'chat'
urlpatterns = [
    url('',  views.about, name='about'),
    url('new_room/', views.new_room, name='new_room'),
    url('<label>/', views.chat_room, name='chat_room'),
]