from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .forms import CalendarForm, UserForm
from .models import User, Room, Calendar
# from django.contrib.auth import views as auth_views

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


def read(reqeust):
    '''
    schedule 목록
    '''
    schedule_list = Calendar.objects.order_by('regdate')
    context = {'schedule_list': schedule_list}
    return render(reqeust, 'scheduler/scheduler/read.html', context)

def create(request):
    '''
    schedule 등록
    '''
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.save()
            return redirect ('scheduler:schedule_read')
    else:
        form = CalendarForm()
    context = {'form': form}
    return render(request, 'scheduler/scheduler/create.html', context)