from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import connections
from .forms import NameForm, ChangePassword, LoginData, RegisterForm
from PlanScheduler import settings
from .forms import *
from .models import *
from .optymalization import *

from django.shortcuts import redirect

# Main page

def index(request):
    #planId = 1
    #shiftTime = Time.objects.filter(planId_id=planId).using('schoolsDB')[5].id
    #print(shiftTime)
    print(100*'$')
    #solve_linear_problem()
    return render(request, 'scheduler/mainpage.html')


# Account pages---------------------------------

@login_required
def myplan(request):
    print(30 * 'W')
    current_user = request.user
    print(current_user.id)
    return render(request, 'scheduler/myplans.html')


@login_required
def createPlan(request):
    # if request.method == 'POST':
    # form = PlanNameForm(request.POST)
    # if form.is_valid():
    # pass
    # p = Time.objects.using(planName).create(timeWindow=selectedTime)
    # p.save(using=planName)

    print(150 * '*')
    # else:
    # form = PlanNameForm()
    return render(request, 'scheduler/instruction.html')


@login_required
def account(request):
    return render(request, 'scheduler/login.html', {'form': form})

@login_required
def datasets(request):
    pass


# <<Undone>> start

# Filling data------------------------------------------

#@login_required
def namePlan(request):
    if request.method == 'POST':
        form = PlanNameForm(request.POST)
        if form.is_valid():
            actualUser = str(request.user)
            planName = form.cleaned_data['planName']
            assign = PlansPermission.objects.using('schoolsDB').create(userData=actualUser, planName=planName)
            assign.save(using='schoolsDB')
            planObject = PlansPermission.objects
            planId = planObject.filter(planName=planName).using('schoolsDB')[0].id
            return redirect('addtime', planId=planId)
    else:
        form = PlanNameForm()
    return render(request, 'scheduler/instruction.html')

@csrf_exempt
@login_required
def addTime(request, planId):
    plan = PlansPermission.objects.filter(id=planId).using('schoolsDB')[0].planName
    if request.method == 'POST':
        monday = request.POST.getlist('mondayHours')
        tuesday = request.POST.getlist('tuesdayHours')
        wednesday = request.POST.getlist('wednesdayHours')
        thursday = request.POST.getlist('thursdayHours')
        friday = request.POST.getlist('fridayHours')
        saturday = request.POST.getlist('saturdayHours')
        sunday = request.POST.getlist('sundayHours')
        data = None
        for hour in monday:
            data = Time.objects.using('schoolsDB').create(planId_id=planId, timeWindow=hour, day='monday')
        for hour in tuesday:
            data = Time.objects.using('schoolsDB').create(planId_id=planId, timeWindow=hour, day='tuesday')
        for hour in wednesday:
            data = Time.objects.using('schoolDB').create(planName_id=planId, timeWindow=hour, day='wednesday')
        for hour in thursday:
            data = Time.objects.using('schoolDB').create(planName_id=planId, timeWindow=hour, day='thursday')
        for hour in friday:
            data = Time.objects.using('schoolDB').create(planName_id=planId, timeWindow=hour, day='friday')
        for hour in saturday:
            data = Time.objects.using('schoolDB').create(planName_id=planId, timeWindow=hour, day='saturday')
        for hour in sunday:
            data = Time.objects.using('schoolDB').create(planName_id=planId, timeWindow=hour, day='sunday')
        if data is not None:
            data.save(using='schoolsDB')
            return redirect(addClasses, planId)
    return render(request, 'scheduler/addtime.html', {'allDay': (range(1, 25)), 'plan':plan})


#@login_required
def addClasses(request, planId):
    data = None
    if request.method == 'POST':
        form = AddClassesForm(request.POST)
        if form.is_valid():

            groupName = form.cleaned_data['groupName']
            minDayHours = form.cleaned_data['minDayHours']
            maxDayHours = form.cleaned_data['maxDayHours']
            
            data = Group.objects.using('schoolsDB').create(groupName=groupName, minDailyHoursClass=minDayHours, maxDailyHoursClass=maxDayHours, planId_id=planId)
            data.save(using="schoolsDB")

    else:
        form = AddClassesForm()
    return render(request, 'scheduler/addclass.html', {'planId':planId})


@login_required
def addTeacher(request, planId):
    if request.method == 'POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            minDayHours = form.cleaned_data['minDayHours']
            maxDayHours = form.cleaned_data['maxDayHours']
            minWeekHours = form.cleaned_data['minWeekHours']
            maxWeekHours = form.cleaned_data['maxWeekHours']
            
            data = Teacher.objects.using('schoolsDB').create(planId_id=planId, name=name, surname=surname,
                                                            minDailyHours=minDayHours, maxDailyHours=maxDayHours,
                                                            minWeeklyHours=minWeekHours, maxWeeklyHours=maxWeekHours)
            data.save(using="schoolsDB")
    else:
        form = AddTeacherForm()
    return render(request, 'scheduler/addteacher.html')


@login_required
def addLesson(request, planId):
    data = None
    if request.method == 'POST':
        form = AddLessonForm(request.POST)
        if form.is_valid():
            lessonName = form.cleaned_data['lessonName']
            data = Lesson.objects.using('schoolsDB').create(planId_id=planId, lessonName=lessonName)
            data.save(using='schoolsDB')
    else:
        form = AddLessonForm()
    return render(request, 'scheduler/addlesson.html', {'planId':planId})


@login_required
def addClassroom(request, planId):
    data=None
    if request.method == 'POST':
        form = AddClassroomForm(request.POST)
        if form.is_valid():
            classroomName = form.cleaned_data['classroomName']
            building = form.cleaned_data['building']
            data = Classroom.objects.using('schoolsDB').create(planId_id=planId, classroomName=classroomName, building=building)
            data.save(using='schoolsDB')
    else:
        form = AddClassroomForm()
    return render(request, 'scheduler/addclassroom.html')


# Connect---------------------------------------
#@login_required
def connectClasses(request, planId, inter):

    teachers = Teacher.objects.filter(planId_id=planId).using('schoolsDB')
    lessons = Lesson.objects.filter(planId_id=planId).using('schoolsDB')
    classrooms = Classroom.objects.filter(planId_id=planId).using('schoolsDB')
    times = Time.objects.filter(planId_id=planId).using('schoolsDB')
    groups = Group.objects.filter(planId_id=planId).using('schoolsDB')

    group = groups[inter]
    inter += 1

    if request.method == 'POST':
        groupTeacher = request.POST.getlist('groupTeacher')
        groupLesson = request.POST.getlist('groupLesson')
        groupClassroom = request.POST.getlist('groupClassroom')
        groupTime = request.POST.getlist('groupTime')

        for teacher in groupTeacher:
            group.teacher.add(teacher)
        for lesson in groupLesson:
            group.lesson.add(lesson)
        for classroom in groupClassroom:
            group.classroom.add(classroom)
        for time in groupTime:
            group.time.add(time)

        if inter<len(groups):
            return redirect(connectClasses, planId=planId, inter=inter)
    return render(request, 'scheduler/connectclasses.html',
                      {'teachers':teachers, 'lessons':lessons,'classrooms':classrooms, 'times':times, 'groups':groups})


#@login_required
def connectTeachers(request, planId, inter):
    print(100*";")
    print(planId, inter)

    lessons = Lesson.objects.filter(planId_id=planId).using('schoolsDB')
    classrooms = Classroom.objects.filter(planId_id=planId).using('schoolsDB')
    times = Time.objects.filter(planId_id=planId).using('schoolsDB')
    teachers = Teacher.objects.filter(planId_id=planId).using('schoolsDB')
    teacher = teachers[inter]
    inter += 1

    if request.method == 'POST':
        teacherLessons = request.POST.getlist('teacherLessons')
        teacherClassroom = request.POST.getlist('teacherClassroom')
        teacherTime = request.POST.getlist('teacherTime')

        for selectLesson in teacherLessons:
            teacher.lesson.add(selectLesson)
        for selectClassroom in teacherClassroom:
            teacher.classroom.add(selectClassroom)
        for selectTime in teacherTime:
            teacher.time.add(selectTime)

        if inter<len(teachers):
            return redirect(connectTeachers, planId=1, inter=inter)
    return render(request, 'scheduler/connectteachers.html',
                  {'lessons':lessons, 'classrooms':classrooms, 'times':times, 'teacher':teacher})


#@login_required
def connectLessons(request, planId, inter):
    classrooms = Classroom.objects.filter(planId_id=planId).using('schoolsDB')
    times = Time.objects.filter(planId_id=planId).using('schoolsDB')
    lessons = Lesson.objects.filter(planId_id=planId).using('schoolsDB')
    lesson = lessons[inter]
    inter += 1

    if request.method == 'POST':
        lessonClassroom = request.POST.getlist('lessonClassroom')
        lessonTime = request.POST.getlist('lessonTime')

        for selectLesson in lessonClassroom:
            lesson.classrooms.add(selectLesson)
        for selectTime in lessonTime:
            lesson.time.add(selectTime)

        if inter<len(teachers):
            return redirect(connectLessons, planId=1, inter=inter)
    return render(request, 'scheduler/instruction.html',
                  {'classrooms':classrooms, 'times':times})

#@login_required
def connectClassrooms(request):
    times = Time.objects.filter(planId_id=planId).using('schoolsDB')
    classrooms = Classroom.objects.filter(planId_id=planId).using('schoolsDB')
    classroom = classrooms[inter]
    inter += 1

    if request.method == 'POST':
        classroomTime = request.POST.getlist('classroomTime')

        for selectTime in classroomTime:
            classroom.time.add(selectTime)

        if inter<len(classrooms):
            return redirect(connectClassrooms, planId=1, inter=inter)
    return render(request, 'scheduler/instruction.html',
                  {'times':times})


# Generate plan --------------------------

#@login_required
def generate(request):
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            pass
    else:
        form = NameForm()
    return render(request, 'scheduler/instruction.html')


# <<Undone>> end

# User settings--------------------

@csrf_exempt
def getin(request):
    print(100 * 'k')
    if request.method == 'POST':
        form = LoginData(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            print(60 * '&')
            print(username)
            user = authenticate(request, username=username, password=pas)
            if user is not None:
                login(request, user)
                print(30 * '-')
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
            if (str(password) == str(rePassword)):
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
            if (newPass == newRePass):
                # user = User.objects.get(username='john')
                # user.set_password('new password')
                # user.save()
                return render(request, 'scheduler/login.html', {'form': form})
    else:
        form = ChangePassword()
    return render(request, "scheduler/changepassword.html", {'form': form})


@login_required
def logout(request):
    logout(request)
    return render(request, 'scheduler/mainpage.html')
