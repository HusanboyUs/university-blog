from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_view, name='list-view'),
  path('detail/<int:pk>/', views.detail_view, name='detail_view'),
  path('about/', views.BlogAboutView, name='about-view'),
]
