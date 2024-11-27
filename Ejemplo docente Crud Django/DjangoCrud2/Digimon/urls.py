from django.urls import path
from . import views

# This code snippet is defining URL patterns for a Django web application. Each `path` function call
# represents a URL pattern that maps a specific URL to a corresponding view function.
urlpatterns = [
  path('', views.digimon_list, name='digimon_list'),
  path('digimon/<int:pk>/', views.digimon_detail, name='digimon_detail'),
  path('digimon/new/', views.digimon_new, name='digimon_new'),
  path('digimon/<int:pk>/edit/', views.digimon_edit, name='digimon_edit'),
  path('digimon/delete/<int:pk>/', views.digimon_delete, name='digimon_delete'),
]