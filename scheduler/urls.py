from django.urls import path
from . import views

app_name = 'scheduler'

urlpatterns = [
    path('create/', views.create, name = 'schedule_create'),
    path('list/', views.list, name = 'schedule_list'),
    path('list/<int:schedule_num>/', views.detail, name = 'schedule_detail'),
    path('list/update/<int:schedule_num>/', views.update, name = 'schedule_update'),
    path('list/delete/<int:schedule_num>/', views.delete, name = 'schedule_delete'),
    # ----------------------------------------------------------------------------
    path('', views.index, name = 'index'), # 첫 화면 일정 리스트
    path('schedule/', views.schedule, name = 'schedule'), # 달력 스케줄
    # ----------------------------------------------------------------------------
    # path('test/', views.test, name = 'test'), # 달력 스케줄
    path('calendar_list/', views.calendar_list, name = 'calendar_list'), # 달력 스케줄
]
