from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import NameForm

from django.views.decorators.csrf import csrf_exempt

list = []

def index(request):
    template = loader.get_template('scheduler/addclass.html')
    context = {"last word": "w"}
    return HttpResponse(template.render(context, request))


def register(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print('aaaaaaaaaaaaaaaaaa')
            username = form.cleaned_data['username']
            pas = form.cleaned_data['pas']
            list.append(username)
            user = User.objects.create_user(username, "", pas)
            user.save()
            print(30 * '+')
            print("user created")
            return render(request, 'scheduler/login.html', {'form': form})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'scheduler/login.html', {'form': form})
    #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    #user.last_name = 'Lennon'
    #user.save()


def changePassword(request):
    #u = User.objects.get(username='john')
    #u.set_password('new password')
    #u.save()
    return render(request, "scheduler/changepassword.html")

@csrf_exempt
def login(request):
    print(30*'+')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        # create a form instance and populate it with data from the request:
        # form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = form.cleaned_data['username']
            pas = form.cleaned_data['pas']
            user = authenticate(username=username, password=pas)
            if user is not None:
                print(30*'-')
                print('log in')
                myplan(request)
                return HttpResponseRedirect('myplans')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            #DZIAAAAAAALAAAAAAA
            return render(request, 'scheduler/login.html', {'form': form})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()


    return render(request, 'scheduler/login.html', {'form': form})

def logout(request):
    logout(request)

def user(request, username):
    username = request.POST['Password']
    if username=="aaa":
        return render(request, "scheduler/addclass.html")

def error(request):
    return render(request, "scheduler/myplans.html")

def fail(request):
    return render(request, "scheduler/index.html")

def success(request):
    return render(request, "scheduler/index.html")

def myplan(request):
    print(30*'W')
    return render(request, 'scheduler/myplans.html')

def account(request):
    return render(request, 'scheduler/login.html', {'form': form})