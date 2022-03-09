from django.urls import path
from . import views

urlpatterns = [
    # path('', views.PostView.as_view(), name = 'post_list'),
    # path('post/<int:num>', views.PostView.as_view(), name = 'post_detail'),
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('signin', views.signin, name = 'signin'),
    path('schedule', views.schedule, name = 'schedule'),
]
