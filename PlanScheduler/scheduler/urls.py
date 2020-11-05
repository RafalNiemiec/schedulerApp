from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('error', views.error, name='error'),

    path('myplans', views.myplan, name='myplans'),
    #path('account', views.account, name='account'),
    path('changepassword', views.changePassword, name='changePassword'),

    #results
    path('successful', views.success, name='success'),
    path('fail', views.fail, name='fail'),
]