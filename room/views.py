from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from scheduler.models import Room, UserInRoom, User
from scheduler.forms import RoomForm

def path_type(request):
    if request.path.split('/')[-1] == 'room':
        return 'Room'
    elif str.isdecimal(request.path.split('/')[-1]) and request.path.split('/')[-2] == 'enter':
        return 'scheduler'

# Create your views here.
@api_view(['POST'])
def join_room(request, room_num):
    user_num = request.POST['user_num']
    
    if UserInRoom.objects.filter(room_num=room_num, user_num=user_num).exists():
        return redirect('/')
    
    user_in_room = UserInRoom(
        user_num = user_num,
        room_num = room_num
    )
    
    user_in_room.save()
    
    return redirect('/?success=2')

@api_view(['POST'])
def out_room(request, room_num):
    user_num = request.POST['user_num']
    
    UserInRoom.objects.filter(room_num=room_num, user_num=user_num).delete()
    
    return redirect('/?success=3')
    
@api_view(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        roomForm = RoomForm
        context = {
            'path_type': path_type(request),
            'roomForm': roomForm
        }
        return render(request, 'scheduler/room/edit.html', context)
    elif request.method == 'POST':
        title = request.POST['title']
        master = request.POST['master']
        invite = list(map(str.strip, request.POST['invite'].split(',')))
        
        users = User.objects.filter(nickname__in=invite)
        
        users_num = list(filter(lambda z: z != int(master), list(map(lambda x: x.get('num'), users.values()))))
        
        print(users_num)
        
        room = Room(
            master=master,
            title=title,
        )

        room.save()
        
        userInRoom = UserInRoom(
            room_num_id=room.pk,
            user_num_id=master,
        )
        userInRoom.save()
        
        for i in users_num:
            UserInRoom(
                room_num_id=room.pk,
                user_num_id=i
            ).save()
        
        return redirect('/')
    
@api_view(['GET', 'POST'])
def edit(request, room_num):
    room = Room.objects.get(num=room_num)
    
    if request.method == 'POST':
        if not request.POST['master']:
            return redirect('/?error=4')
        room.title = request.POST['title']
        room.master = request.POST['master']
        room.save()
        
        invite = list(map(str.strip, request.POST['invite'].split(',')))
        
        users = User.objects.filter(nickname__in=invite)
        
        users_num = list(map(lambda x: x.get('num'), users.values()))
        
        for i in users_num:
            UserInRoom(
                room_num_id=room.pk,
                user_num_id=i
            ).save()
        
        return redirect('scheduler:index')
    else:
        if Room.objects.filter(num=room_num).exists():
            context = {
                'roomForm': RoomForm(instance=room),
                'room': room
            }
            return render(request, 'scheduler/room/edit.html', context)
        else: return redirect('/?error=3')

@api_view(['POST'])
def delete(request, room_num):
    room = Room.objects.filter(num=room_num)
    
    uir = UserInRoom.objects.filter(room_num=room_num)
    
    if room.exists(): room.delete()
    if uir.exists(): uir.delete()
    
    return redirect('scheduler:index')
    
@api_view(['GET'])
def enter_room(request, room_num):
    
    context = {
        'path_type': path_type(request),
        'room_num': room_num
    }
    
    return render(request, 'scheduler/schedule.html', context)