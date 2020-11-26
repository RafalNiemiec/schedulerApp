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

    path('instruction', views.namePlan, name='instruction'),
    path('addtime/<int:planId>', views.addTime, name='addtime'),
    path('addclasses/<int:planId>', views.addClasses, name='addclasses'),
    path('addteacher/<int:planId>', views.addTeacher, name='addteacher'),
    path('addlesson/<int:planId>', views.addLesson, name='addlesson'),
    path('addclassroom/<int:planId>', views.addClassroom, name='addclassroom'),
    #"""
    
    #Connect data
    #"""
    #path('instruction', views.connectPlan, name='instruction')
    #path('connecttime', views.connectTime, name='connecttime')
    path('connectclasses/<int:planId>/<int:inter>', views.connectClasses, name='connectclasses'),
    path('connectteacher/<int:planId>/<int:inter>', views.connectTeachers, name='connectteacher'),
    path('connectlesson/<int:planId>/<int:inter>', views.connectLessons, name='connectlesson'),
    path('connectclassroom/<int:planId>/<int:inter>', views.connectClassrooms, name='connectclassroom'),
    #"""

    #path('generate', views.generate, name='generate')

]