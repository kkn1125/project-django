from calendar import calendar
from django.shortcuts import render, redirect
from django.utils import timezone
from rest_framework.decorators import api_view
from .forms import CalendarForm
from .models import User, Room, Calendar
# from django.contrib.auth import views as auth_views

def path_type(request):
    if request.path.split('/')[-1] == '':
        return 'Home'
    elif request.path.split('/')[-1] == 'schedule':
        return 'Schedule'

@api_view(['GET'])
def index(request):
    room_list = Room.objects.order_by('regdate')
    
    context = {
        'path_type': path_type(request),
        'room_list': room_list,
    }
    
    return render(request, 'scheduler/index.html', context)

@api_view(['GET'])
def schedule(request):
    user = User.objects.all()
    
    context = {
        'path_type': path_type(request),
        'schedule': user
    }

    return render(request, 'scheduler/schedule.html', context)

def list(reqeust):
    '''
    schedule 목록
    '''
    schedule_list = Calendar.objects.order_by('regdate')
    context = {'schedule_list': schedule_list}
    return render(reqeust, 'scheduler/scheduler/list.html', context)

def create(request):
    '''
    schedule 등록
    '''
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.save()
            return redirect ('scheduler:schedule_create')
    else:
        form = CalendarForm()
    context = {'form': form}
    return render(request, 'scheduler/scheduler/create.html', context)

def detail(request, schedule_num):
    '''
    schedule 내용 출력
    '''
    schedule = Calendar.objects.get(num=schedule_num)
    context = {'schedule': schedule}
    return render(request, 'scheduler/scheduler/detail.html', context)

def update(request, schedule_num):
    '''
    schedule 내용 수정
    '''
    calendar = Calendar.objects.get(pk=schedule_num)
    if request.method == 'POST':
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.updates = timezone.now()
            calendar.save()
            return redirect ('scheduler:schedule_detail', schedule_num=calendar.num)
    else:
        form = CalendarForm(instance=calendar)
    context = {'form': form}
    return render(request, 'scheduler/scheduler/create.html', context)

def delete(request, schedule_num):
    '''
    schedule 삭제
    '''
    calendar = Calendar.objects.get(pk=schedule_num)
    calendar.delete()
    return redirect('scheduler:schedule_list')
