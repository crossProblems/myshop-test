import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import *
from .models import ImgFile

# Create your views here.
def upload_file(request):
    if request.method == "GET":
        return render(request, "5/upload.html")
    if request.method == "POST":
        myFile = request.FILES.get("myfile", None)
        if myFile:
            path = 'media/uploads/'
            if not os.path.exists(path):
                os.makedirs(path)
            dest = open(os.path.join(path+myFile.name), 'wb+')
            for chunk in myFile.chunks():
                dest.write(chunk)
                dest.close()
            return HttpResponse("上传完成")
        else:
            return HttpResponse("没有上传文件")

def userinfo_form(request):
    if request.method == "GET":
        myform = UserInfoForm()
        return render(request, "5/userinfo.html", {'form_obj': myform})

def userinfo_msg_form(request):
    if request.method == "GET":
        myform = UserInfo_Msg_Form()
        return render(request, "5/userinfoform.html", {'form_obj': myform})
    else:
        f = UserInfo_Msg_Form(request.POST)
        if f.is_valid():
            print(f.cleaned_data["username"])
        else:
            errors = f.errors
            print(errors)
            return render(request, "5/userinfoform.html", {'form_obj': f, 'errors': errors})
        return render(request, "5/userinfoform.html", {'form_obj': f})

def imgfileform(request):
    if request.method == "GET":
        f = ImgFileForm()
        return render(request, "5/upload_form.html", {'form_obj': f})
    else:
        f = ImgFileForm(request.POST, request.FILES)
        if f.is_valid():
            name = f.cleaned_data['name']
            headimg = f.cleaned_data['headimg']
            userimg = ImgFile()
            userimg.name = name
            userimg.headimg = headimg
            userimg.save()
            print('上传成功')
            return render(request, "5/upload_form.html", {'form_obj': f, 'user': userimg})

def ajax_login(request):
    f = AjaxLoginForm()
    return render(request, "5/ajax_login.html", {'form_obj': f})

def ajax_login_data(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == '123456':
        return JsonResponse({'code': 1, 'msg': '登陆成功'})
    else:
        return JsonResponse({'code': 0, 'msg': '登录失败'})