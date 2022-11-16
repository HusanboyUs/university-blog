from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_blog_api, name='list-view_api'),
  path('detail/<int:pk>/', views.detail_blog_api, name='list-view_api'),
]
