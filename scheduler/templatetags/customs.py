from django import template
from ..models import User, UserInRoom
from django.core import serializers

register = template.Library()

@register.simple_tag
def set(value=None):
    return value

"""
회원 넘버로 조회하는 필드들
"""
@register.filter(name='user_profile')
def user_profile(value, key=''):
    if not value:
        return key
    user = User.objects.filter(pk=value)
    if user.exists():
        profile = user.get(pk=value).profile
        if str.strip(str(profile)):
            return '/media/{0}'.format(str(profile))
        else:
            return key
    return key

@register.filter(name='user_nickname')
def user_nickname(value, key=''):
    if not value:
        return key
    user = User.objects.filter(pk=value)
    if user.exists():
        nickname = user.get(pk=value).nickname
        return nickname
    return key

@register.filter(name='user_email')
def user_email(value, key=''):
    if not value:
        return key
    user = User.objects.filter(pk=value)
    if user.exists():
        email = user.get(pk=value).email
        return email
    return key
"""
회원 넘버로 조회하는 필드들
"""

@register.filter(name='form_value')
def form_value(value, key):
    print(key)
    keys = key.split('/')[0]
    vals = key.split('/')[1]
    print(vals)
    value.initial.setdefault(keys, str(vals))
    return value

@register.filter(name='is_number')
def is_number(value):
    return not str.isdecimal(value)

@register.filter(name='split')
def split(value, key):
    return value.split(key)

@register.filter(name='arr_trim')
def arr_trim(value, key):
    return list(filter(lambda x: x != key, value))

@register.filter(name='capitalize')
def capitalize(value):
    return value.capitalize()

@register.filter(name='first_word')
def first_word(value):
    if value:
        return value[0]
    else:
        return value

@register.filter(name='room_user')
def room_user(value):
    temp = UserInRoom.objects.filter(room_num=value)
    if temp.exists():
        users = [i.get('user_num_id') for i in list(temp.values())]
        return users
    return ''

@register.filter(name='to_nickname')
def to_nickname(value):
    temp = User.objects.filter(num__in=value)
    if temp.exists():
        users = [i.get('nickname') for i in list(temp.values())]
        return users
    return ''

@register.filter(name='user_in_room_count')
def user_in_room_count(value):
    temp = UserInRoom.objects.filter(user_num_id=value)
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
    temp = UserInRoom.objects.filter(room_num_id=value)
    if temp.exists():
        return temp.count()
    return ''

@register.filter(name='is_crew')
def is_crew(value, key):
    temp = UserInRoom.objects.filter(room_num_id=value)
    filtered = [item for item in temp.values() if item['user_num_id'] == key]

    if len(filtered) > 0:
        return True
    return False