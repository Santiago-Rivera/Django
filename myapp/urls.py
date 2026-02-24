from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<int:id>', views.hello_world),
]
