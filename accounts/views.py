from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login, logout


def index(request):
    context = {'user': request.user}
    return render(request, 'index.html', context)


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(username=username, password=password)
    new_user.save()
    return HttpResponseRedirect('home')


def signin(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponseRedirect('home')

    if user.password == password:
        login(request, user)  # これを実行するとユーザをログイン状態にできる
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('home')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
