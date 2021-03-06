from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('room', views.create, name='create'),
    path('room/<int:room_num>', views.edit, name='edit'),
    path('room/del/<int:room_num>', views.delete, name='delete'),
    path('join/<int:room_num>', views.join_room, name='join'),
    path('out/<int:room_num>', views.out_room, name='out'),
    path('enter/<int:room_num>', views.enter_room, name='enter'),
]
