from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:id>/', views.hello_world, name='hello_world'),
    path('about/', views.about, name='about'),
]