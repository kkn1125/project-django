from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from django.contrib.auth import views as auth_views
from .forms import UserForm
from .models import User, Room

def path_type(request):
    if request.path.split('/')[-1] == '':
        return 'Home'
    elif request.path.split('/')[-1] == 'schedule':
        return 'Schedule'

# Create your views here.
@api_view(['GET'])
def index(request):
    room_list = Room.objects.order_by('regdate')
    
    context = {
        'path_type': path_type(request),
        'room_list': room_list,
    }
    
    return render(request, 'scheduler/index.html', context)

# @api_view(['GET'])
# def schedule(request):
#     user = User.objects.all()
    
#     context = {
#         'path_type': path_type(request),
#         'schedule': user
#     }

#     return render(request, 'scheduler/schedule.html', context)