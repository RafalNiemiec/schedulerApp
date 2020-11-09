from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#from .forms import NameForm, ChangePassword, LoginData, RegisterForm
#from .models import Group, Teacher, Lesson, Classroom, Time,
                    #GroupTeacher, GroupLesson, GroupClassroom, GroupTime,
                    #TeacherLesson, TeacherClassroom, TeacherTime,
                    #LessonC
from .forms import *

#Main page

def index(request):

    return render(request, 'scheduler/mainpage.html')


#Account pages

@login_required
def myplan(request):
    print(30*'W')
    current_user = request.user
    print(current_user.id)
    return render(request, 'scheduler/myplans.html')

@login_required
def createPlan(request):
    if request.method == 'POST':
        #form = (request.POST)
        if form.is_valid():
            pass
    else:
        form = ChangePassword()
    return render(request, 'scheduler/instruction.html')

@login_required
def account(request):
    return render(request, 'scheduler/login.html', {'form': form})

@login_required
def datasets(request):
    pass


#<<Undone>> start

#Filling data

@login_required
def namePlan():
    if request.method == 'POST':
        form = PlanNameForm(request.POST)
        if form.is_valid():
            pass
            #planName = form.cleaned_data['planName']
            #Create new database with name: planname
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def addTime(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def addClasses():
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def addTeacher():
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def addLesson(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def addClassroom(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

#Connect

@login_required
def connectClasses():
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def connectTeachers(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def connectLessons(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

@login_required
def connectClassrooms(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')

#Generate plan

@login_required
def generate(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')


#<<Undone>> end

#User settings

@csrf_exempt
def getin(request):
    print(100*'k')
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            print(60*'&')
            print(username)
            user = authenticate(request, username=username, password=pas)
            if user is not None:
                login(request, user)
                print(30*'-')
                print('log in')
                myplan(request)
                return HttpResponseRedirect('myplans')
            return render(request, 'scheduler/login.html', {'form': form})
    else:
        form = NameForm()
    return render(request, 'scheduler/login.html', {'form': form})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            rePassword = form.cleaned_data['password']
            if (str(password)==str(rePassword)):
                user = User.objects.create_user(username, "", password)
                user.save()
                print(30 * '+')
                print("user created")
                return render(request, 'scheduler/login.html', {'form': form})
            else:
                print("Passwords are not equal")
    else:
        form = RegisterForm()
    return render(request, 'scheduler/register.html', {'form': form})

@login_required
def changePassword(request):
    if request.method == 'POST':
        form = ChangePassword(request.POST)
        if form.is_valid():
            currPass = form.cleaned_data['currPass']
            newPass = form.cleaned_data['newPass']
            newRePass = form.cleaned_data["newRePass"]
            if (newPass==newRePass):
                #user = User.objects.get(username='john')
                #user.set_password('new password')
                #user.save()
                return render(request, 'scheduler/login.html', {'form': form})
    else:
        form = ChangePassword()
    return render(request, "scheduler/changepassword.html", {'form': form})

@login_required
def logout(request):
    logout(request)
    return render(request, 'scheduler/mainpage.html')






















def error(request):
    return render(request, "scheduler/myplans.html")

def fail(request):
    return render(request, "scheduler/index.html")

def success(request):
    return render(request, "scheduler/index.html")

