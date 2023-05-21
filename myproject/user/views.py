from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore
from .models import Myuser
from django.contrib.auth.decorators import login_required


@login_required
def getAllUsers(request):
    data = Myuser.objects.all()
    return render(request, 'allUser.html', {'data': data})


def register(request):
    return render(request, 'register.html')


def registerAddUser(request):
    if request.method == 'POST':
        Myuser.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password'],
            age=request.POST['age']
        )
        return HttpResponseRedirect("/")


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = Myuser.objects.filter(email=email, password=password).first()

        if user is not None:
            request.session['name'] = user.name
            return HttpResponseRedirect("/user/home/")
        else:
            context = {
                'msg': 'Invalid email or password'
            }
            return render(request, 'login.html', context)


@login_required
def editUser(request, user_id):
    user = Myuser.objects.get(id=user_id)
    return render(request, 'editUser.html', {'user': user})


@login_required
def updateUser(request, user_id):
    if request.method == 'POST':
        user = Myuser.objects.get(id=user_id)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.age = request.POST['age']
        user.save()
        return redirect('/user/users/')
    else:
        user = Myuser.objects.get(id=user_id)
        return render(request, 'editUser.html', {'user': user})


@login_required
def deleteUser(request, user_id):
    user = Myuser.objects.get(id=user_id)
    user.delete()
    return redirect('/user/users/')


@login_required
def home(request):
    return render(request, 'parent.html')
