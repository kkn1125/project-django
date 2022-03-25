from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.utils import timezone
from rest_framework.decorators import api_view
from .forms import CalendarForm
from .models import User, Room, Calendar
from django.core import serializers
from django.http import JsonResponse, HttpResponse

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

def calendar_list(reqeust, num):
    '''
    schedule 목록
    '''
    schedule_list = Calendar.objects.filter(room_num_id=num).order_by('regdate')
    
    # 밑에 과정들
    # https://dev-yakuza.posstree.com/ko/django/response-model-to-json/ [ 참조 ]
    
    list = serializers.serialize('json', schedule_list)
    return HttpResponse(list, content_type="text/json-comment-filtered")

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
        start_date = request.POST['start_date']
        start_time = request.POST['start_time']

        if form.is_valid():
            calendar = form.save(commit=False)
            
            calendar.start_date = str(calendar.start_date).replace('+09:00','+00:00')
            calendar.end_date = str(calendar.end_date).replace('+09:00','+00:00')
            
            calendar.save()
            
            return redirect ('room:enter', room_num=calendar.room_num_id)
    else:
        form = CalendarForm()
    context = {'form': form}
    return render(request, 'scheduler/scheduler/create.html', context)

def detail(request, schedule_num):
    '''
    schedule 내용 출력
    '''
    schedule = Calendar.objects.filter(pk=schedule_num).get(pk=schedule_num)
    context = {'schedule': schedule}
    return render(request, 'scheduler/scheduler/detail.html', context)

def update(request, schedule_num):
    '''
    schedule 내용 수정
    '''
    calendar = Calendar.objects.filter(pk=schedule_num).get(pk=schedule_num)
    if request.method == 'POST':
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            calendar = form.save(commit=False)
            # calendar.updates = timezone.now()
            calendar.save()
            return redirect ('scheduler:schedule_detail', schedule_num=calendar.pk) # pk === num
    else:
        form = CalendarForm(instance=calendar)
    context = {'form': form}
    return render(request, 'scheduler/scheduler/create.html', context)

def delete(request, schedule_num):
    '''
    schedule 삭제
    '''
    Calendar.objects.filter(pk=schedule_num).delete()
    return redirect('scheduler:schedule_list')
