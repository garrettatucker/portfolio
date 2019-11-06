from . import views
from django.urls import path, include

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about.html/', views.AboutPageView.as_view(), name='about'),
]