from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #User operations
    path('register', views.register, name='register'),
    path('login', views.getin, name='login'),
    path('logout', views.logout, name='logout'),
    #path('account', views.account, name='account'),

    #Account
    path('myplans', views.myplan, name='myplans'),
    #"""
    #path('changepassword', views.changePassword, name='changePassword'),
    #path('account', views.account, name='account'),
    #path('data', views.account, name='data'),
    #"""
    
    #Filling data

    path('instruction', views.namePlan, name='instruction')
    #path('addtime', views.addTime, name='addtime')
    #path('addclasses', views.addClasses, name='addclasses')
    #path('addteacher', views.addTeacher, name='addteacher')
    #path('addlesson', views.addLesson, name='addlesson')
    #path('addclassroom', views.addClassroom, name='addclassroom')
    #"""
    
    #Connect data
    #"""
    #path('instruction', views.connectPlan, name='instruction')
    #path('connecttime', views.connectTime, name='connecttime')
    #path('connectclasses', views.connectClasses, name='connectclasses')
    #path('connectteacher', views.connectTeacher, name='connectteacher')
    #path('connectlesson', views.connectLesson, name='connectlesson')
    #path('connectclassroom', views.connectClassroom, name='connectclassroom')
    #"""

    #path('generate', views.generate, name='generate')

]