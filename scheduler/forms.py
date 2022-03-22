from django import forms
from django.forms import ModelForm, NumberInput
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'profile', 'nickname', 'email', 'password'
            ]
        
class LoginForm(ModelForm):
    # email = forms.CharField(required=False)
    # password = forms.CharField(required=False)
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@" not in data:
            raise forms.ValidationError("이메일 형식과 다릅니다.")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data
    
    class Meta:
        model = User
        fields = [
            'email', 'password'
            ]
        
class FindForm(ModelForm):
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@" not in data:
            raise forms.ValidationError("이메일 형식과 다릅니다.")

        return data
    
    class Meta:
        model = User
        fields = [
            'nickname', 'email'#, 'password'
            ]
        
class CheckForm(ModelForm):
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@" not in data:
            raise forms.ValidationError("이메일 형식과 다릅니다.")

        return data
    
    class Meta:
        model = User
        fields = [
            'email'#, 'password'
            ]
    
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'title'
            ]

class UserInRoomForm(ModelForm):
    class Meta:
        model = UserInRoom
        fields = [
            'room_num', 'user_num'
            ]

class CalendarForm(ModelForm):
    class Meta:
        model = Calendar
        fields = [
            'room_num', 'user_num', 'category', 'title', 'schedule', 'coworker', 'start_date', 'end_date'
            ]
        widgets = {
            'schedule': forms.Textarea(attrs={'rows': 10}),
        }