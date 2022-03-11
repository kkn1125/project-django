from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name = 'signup'),
    path('update/<int:num>', views.update, name = 'update'),
    path('signout', views.signout, name="signout"),
    path('unsign/<int:num>', views.unsign, name="unsign")
]