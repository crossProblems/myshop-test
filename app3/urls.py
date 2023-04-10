from django.urls import path
from app3 import views

urlpatterns = [
    path('var/', views.var),
    path('for_label/', views.for_label),
    path('filter/', views.filter)
]
