from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download, name='download'),
    path('upload/', views.upload, name='upload'),
    path('zip/', views.zip, name='zip'),
]