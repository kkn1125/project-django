from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('auth_reset_pass', views.auth_reset_pass, name='auth_reset_pass'),
    path('finduser', views.find_user, name='finduser'),
    path('send_mail', views.send_mail, name='send_mail'),
    path('find', views.find, name='find'),
    path('reset_pass', views.reset_pass, name='reset_pass'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name = 'signup'),
    path('update/<int:num>', views.update, name = 'update'),
    path('signout', views.signout, name="signout"),
    path('unsign/<int:num>', views.unsign, name="unsign")
]