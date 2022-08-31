from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download, name='download'),
    path('upload/', views.download, name='upload'),
    path('zip/', views.download, name='zip'),
]