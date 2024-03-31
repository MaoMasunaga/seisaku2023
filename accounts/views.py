from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth import login, logout
from django.contrib import messages

def index(request):
    context = {'user': request.user}
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'このユーザー名は既に使用されています。別のユーザー名を選択してください。')
        else:
            new_user = CustomUser(username=username, password=password)
            new_user.save()
            messages.success(request, 'アカウントを作成しました。')
            return redirect('index')
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            messages.error(request, 'ユーザーが見つかりません。ユーザー名を確認してください。')
            return render(request, 'index.html')

        if user.password == password:
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'ログインに失敗しました。ユーザー名とパスワードを確認してください。')
            return render(request, 'index.html')

    return render(request, 'index.html')



def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
