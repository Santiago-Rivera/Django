from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html')

def tasks(request):
    #task = Task.objects.get(title=title)
    return render(request, 'tasks.html')