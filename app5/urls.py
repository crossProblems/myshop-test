from django.urls import path, re_path
from app5 import views
from myshop import settings
from django.views.static import serve

urlpatterns = [
    path('upload_file/', views.upload_file),
    path('app5/userinfo/', views.userinfo_form),
    path('app5/userinfoform/', views.userinfo_msg_form),
    path('userimg/', views.imgfileform),
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    path('app5/ajaxlogin/', views.ajax_login),
    path('ajax_login_data/', views.ajax_login_data),
]
