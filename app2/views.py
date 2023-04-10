from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
    return HttpResponse('app2中的index方法')

def show(request, id):
    return HttpResponse("App2中的show方法，参数值为id："+str(id))
def show_uuid(request, id):
    return HttpResponse("app2中的show_uuid,id="+str(id))
def show_slug(request, q):
    return HttpResponse("app2中的show_slug,id="+str(q))
def article_list(request, year):
    return HttpResponse("app2中的article_list, year="+str(year))
def article_page(request, page, key):
    return HttpResponse("app2中的article_page, page="+str(page)+", key="+str(key))
def url_reverse(request):
    #使用reverse()反向解析
    print("在views()函数中使用reverse()方法解析的结果："+reverse("app2_url_reverse")+";"+request.path)
    return render(request,"2/url_reverse.html")
def hello(request):
    return HttpResponse("Hello Django!!!")
def test_get(request):
    print(request.get_host())
    print(request.get_raw_uri())
    print(request.path)
    print(request.get_full_path())
    print(request.method)
    print(request.GET)
    print(request.META["HTTP_USER_AGENT"])
    print(request.META["REMOTE_ADDR"])
    print(request.GET.get('username'))
    return HttpResponse("")
def test_post(request):
    print(request.method)
    print(request.POST.get('username'))
    return render(request, '2/test_post.html')
def test_response(request):
    response = HttpResponse()
    response.write("Hllow django")
    response.write("<br>")
    response.write(response.content)
    response.write("<br>")
    response.write(response['Content-type'])
    response.write("<br>")
    response.write(response.status_code)
    response.write("<br>")
    response.write(response.charset)
    response.write("<br>")
    return response
def test_render(request):
    return render(request, '2/test_render.html', {'info':'hello django'}, content_type="text/html")
def test_redirect_model(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return redirect(user)
def userinfo(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse("id="+str(user.id)+";name="+str(user.username))