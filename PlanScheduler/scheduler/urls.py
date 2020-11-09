from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.getin, name='login'),
    path('error', views.error, name='error'),
    path('logout', views.logout, name='logout'),
    #path('account', views.account, name='account'),


    #Account
    path('myplans', views.myplan, name='myplans'),
    #path('changepassword', views.changePassword, name='changePassword'),
    #path('account', views.account, name='account'),
    #path('data', views.account, name='data'),


    #results
    path('successful', views.success, name='success'),
    path('fail', views.fail, name='fail'),
]