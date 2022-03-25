import ast
from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect
from scheduler.models import User
from scheduler.forms import UserForm, LoginForm, FindForm, CheckForm

from django.core import serializers
from django.http import JsonResponse, HttpResponse

def path_type(request):
    if request.path.split('/')[-1] == 'signin':
        return 'Sign In'
    elif request.path.split('/')[-1] == 'signup':
        return 'Sign Up'
    
# Create your views here.
@api_view(['GET', 'POST'])
def auth_reset_pass(request):
    """
    auth 보안상 파일에 적지 않음.
    과정을 대신 적음.
    1. 메일을 발송할 때 비밀 키를 생성해서 auth_reset_pass링크로 auth키를 파라미터와 같이 주소형식으로 보낸다. 예를 들면
        http://baseurl/common/auth_reset_pass?p=[encodedSecretKey]
    2. 해당 경로로 접속하면 쿼리문을 파싱해서 유효한지 검사한다.
        이때 검사는 encodedSecretKey를 쿠키에 저장해서 링크로 접속 했을 때 쿠키 값과 일치하는지 여부로 판별한다.
    3. 추가적으로 javascript로 localStorage에 보낸 데이터 키 값을 false로 해두고 링크 접속해서 쿠키 판별 후 localStorage에 데이터 키가 있는지 보고 이중으로 판별한다.
    4. 확인되면 비밀번호를 새로 적는 칸을 보여주고 유저가 보낸 이메일의 데이터를 수정한다.
    5. 쿠키를 삭제하고, localStorage의 데이터도 삭제한다.
    """
        
@api_view(['GET'])
def find_user(request):
    user_nicks = [n.strip() for n in ast.literal_eval(request.GET['userlist'])]
    users = User.objects.filter(nickname__in=user_nicks)
    s_user = serializers.serialize('json', users)
    return HttpResponse(s_user, content_type="text/json-comment-filtered")
        
@api_view(['GET', 'POST'])
def send_mail(request):
    if request.method == 'POST':
        checkForm = CheckForm(request.POST)
        if checkForm.is_valid():
            return redirect('/common/reset_pass?check=1')
        else:
            return redirect('/common/reset_pass?error=3')
    
@api_view(['GET', 'POST'])
def find(request):
    findForm = FindForm()
    if request.method == 'POST':
        nickname = request.POST['nickname']
        email = request.POST['email']
        user_nick = User.objects.filter(nickname=nickname)
        user_email = User.objects.filter(email=email)
        if user_nick.exists() or user_email:
            return redirect('/common/find?success=4')
        else:
            return redirect('/common/find?error=2')
    else:
        context = {
            'findForm': findForm
        }
        return render(request, 'scheduler/find.html', context)
    
@api_view(['GET'])
def reset_pass(request):
    checkForm = CheckForm()
    context = {
        'checkForm': checkForm
    }
    return render(request, 'scheduler/reset_pass.html', context)
    
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
                        request.session['sign'] = user.num
                        # {
                        #     # 'nickname': user.nickname,
                        #     # 'email': user.email,
                        #     # 'profile': str(user.profile),
                        #     # 'num': user.num,
                        # }
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
        'userForm': UserForm()
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
    user = User.objects.filter(num=num).get(num=num)
    origin_pass = user.password
    if request.method == 'GET':
        context = {
            'path_type': path_type(request),
            'userForm': UserForm(instance=user),
        }
        return render(request, 'scheduler/signup.html', context)
    else:
        userForm = UserForm(request.POST or None,
                            request.FILES or None,
                            instance=user)
        if userForm.is_valid():
            uf = userForm.save(commit=False) # 여기 하는 중
            if not uf.password:
                uf.password = origin_pass
            request.session['sign'] = uf.num
            # {
            #     'nickname': uf.nickname,
            #     'email': uf.email,
            #     'profile': str(uf.profile),
            #     'num': uf.num,
            # }
            uf.save()
        return redirect('account:update', user.pk)

@api_view(['GET'])
def signout(request):
    request.session['sign'] = ''
    return redirect('/?success=5')

@api_view(['POST'])
def unsign(request, num):
    User.objects.filter(num=num).delete()
    
    request.session['sign'] = ''
    
    return redirect('/?success=2')