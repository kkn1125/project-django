from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def index(request):
    context = {
        'board': 1
    }
    return render(request, 'scheduler/index.html', context)

@api_view(['GET'])
def signup(request):
    context = {
        'board': 1
    }
    return render(request, 'scheduler/signup.html', context)

@api_view(['GET'])
def signin(request):
    context = {
        'board': 1
    }
    return render(request, 'scheduler/signin.html', context)

@api_view(['GET'])
def schedule(request):
    context = {
        'board': 1
    }
    return render(request, 'scheduler/schedule.html', context)