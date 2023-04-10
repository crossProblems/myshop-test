from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

class TestTemplateView(TemplateView):
    #设置模板文件
    template_name = "2/test_templateview.html"
    #重写父类的get_context_data()方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "该变量可以传递到模板"
        return context
    
class TestListView(ListView):
    model = UserBaseInfo
    template_name = "2/test_listview.html"
    context_object_name="users"
    paginate_by=1
    def get_queryset(self):
        userinfo=UserBaseInfo.objects.filter(status=1)
        return userinfo
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["info"] = "ListView变量可以传递到模板"
        return context
class TestDetailView(DetailView):
    model = UserBaseInfo
    template_name = "2/test_detailview.html"
    context_object_name="users"
    pk_url_kwarg="userid"
    