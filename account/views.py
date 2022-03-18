from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from scheduler.models import User
from scheduler.forms import UserForm, LoginForm

def path_type(request):
    if request.path.split('/')[-1] == 'signin':
        return 'Sign In'
    elif request.path.split('/')[-1] == 'signup':
        return 'Sign Up'
    
# Create your views here.
@api_view(['GET', 'POST'])
def signin(request):
    result = True
    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            result = True
            if User.objects.filter(email=email).exists():
                    user = User.objects.get(email=email)
                    if password == user.password:
                        request.session['sign'] = {
                            'nickname': user.nickname,
                            'email': user.email,
                            'profile': str(user.profile),
                            'num': user.num,
                        }
                        return redirect('/?success=1')
                    else:
                        return redirect('./signin?error=1')
            else:
                result = False
                request.session['sign'] = ''
    else:
        form = LoginForm()
        
    context = {
        'path_type': path_type(request),
        'form': form
    }
    
    return render(request, 'scheduler/signin.html', context) if result else redirect('./signin?error=1')

@api_view(['GET', 'POST'])
def signup(request):
    context = {
        'path_type': path_type(request),
    }
    
    if request.method == 'GET':
        return render(request, 'scheduler/signup.html', context)
    else:
        profile = request.FILES['profile']
        nickname = request.POST['nickname']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User(
                profile = profile,
                nickname = nickname,
                email = email,
                password = password
            )
        
        user.save()
        
        return redirect('account:signin')

@api_view(['GET', 'POST'])
def update(request, num):
    user = User.objects.get(num=num)
    
    context = {
        'path_type': path_type(request),
        'user': user
    }
    
    if request.method == 'GET':
        return render(request, 'scheduler/signup.html', context)
    else:
        profile = request.FILES['profile']
        nickname = request.POST['nickname']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User(
                profile = profile,
                nickname = nickname,
                email = email,
                password = password
            )
        
        user.save()
        
        return redirect('account:signin')

@api_view(['GET'])
def signout(request):
    request.session['sign'] = ''
    return redirect('/')

@api_view(['POST'])
def unsign(request, num):
    User.objects.filter(num=num).delete()
    
    request.session['sign'] = ''
    
    return redirect('/?success=2')