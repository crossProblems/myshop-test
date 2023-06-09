from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def user_reg(request):
    if request.method == "GET":
        return render(request, '6/user-reg.html')
    if request.method == "POST":
        uname = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        if User.objects.filter(username=uname):
            info = '用户已存在'
        else:
            d = dict(username=uname, password=pwd, email='111@111.com', is_staff=1, is_active=1, is_superuser=1)
            user = User.objects.create_user(**d)
            info = '注册成功'
        return render(request, '6/user_log.html', {'info': info})
