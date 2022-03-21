from django.urls import path
from . import views

app_name = 'scheduler'

urlpatterns = [
    path('create/', views.create, name = 'schedule_create'),
    path('read/', views.read, name = 'schedule_read'),
    path('', views.index, name = 'index'),
]
