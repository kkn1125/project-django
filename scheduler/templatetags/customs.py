from django import template
from ..models import User, UserInRoom

register = template.Library()

@register.filter(name='capitalize')
def capitalize(value):
    return value.capitalize()

@register.filter(name='first_word')
def first_word(value):
    return value[0]

@register.filter(name='user_in_room_count')
def user_in_room_count(value):
    temp = UserInRoom.objects.filter(user_num=value)
    if temp.exists():
        return temp.count()
    return ''

@register.filter(name='find_user')
def find_user(value):
    temp = User.objects.filter(num=value)
    if temp.exists():
        return temp[0]
    return ''

@register.filter(name='user_count')
def user_count(value):
    temp = UserInRoom.objects.filter(room_num=value)
    if temp.exists():
        return temp.count()
    return ''

@register.filter(name='is_crew')
def is_crew(value, key):
    temp = UserInRoom.objects.filter(room_num=value)
    filtered = [item for item in temp.values() if item['user_num'] == key]

    if len(filtered) > 0:
        return True
    return False