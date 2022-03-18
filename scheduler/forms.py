from django import forms
from django.forms import ModelForm, NumberInput
from .models import *
from django import forms

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

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'room_num', 'user_num', 'category', 'title', 'schedule', 'coworker', 'start_date', 'end_date'#, 'updates'
            ]
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'schedule': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'coworker': forms.TextInput(attrs={'class': 'form-control'}),
        }