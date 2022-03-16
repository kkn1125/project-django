from django.forms import ModelForm, NumberInput
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'profile', 'nickname', 'email', 'password'#, 'updates'
            ]

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'title'#, 'master',  'email', 'password'#, 'updates'
            ]
        # widgets = {
        #     'master': NumberInput(
        #         attrs = {
        #             'hidden': True
        #         }
        #         )
        #     }

class UserInRoomForm(ModelForm):
    class Meta:
        model = UserInRoom
        fields = [
            'room_num', 'user_num'#, 'email', 'password'#, 'updates'
            ]

class CalendarForm(ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'room_num', 'user_num', 'category', 'title', 'schedule', 'coworker', 'start_date', 'end_date'#, 'updates'
            ]
