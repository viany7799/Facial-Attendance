from django.urls import path, include
from . import views
from .views import process_frames

urlpatterns = [
    path('',views.main,name='main'),
    path('index',views.index,name='index'),
    path('home',views.home,name='home'),

    path('process_frames/', process_frames, name='process_frames'),

    path('download/', views.download, name='download'),
    path('filter', views.filter, name='filter'),
    path('table', views.table, name='table'),


]