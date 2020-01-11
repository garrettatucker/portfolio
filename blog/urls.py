from . import views
from django.urls import path, include

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('about.html/', views.AboutPageView.as_view(), name='about'),
]