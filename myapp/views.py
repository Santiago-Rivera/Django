from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request, id):
    print(id)
    return HttpResponse("<h1>Hello %s</h1>" % id)

def about(request):
    return HttpResponse("<h2>About Page</h2>")

def projects(request):
    projects = Project.objects.all()
    return JsonResponse({"projects": list(projects.values())})

def tasks(request, title):
    task = Task.objects.get(title=title)
    return HttpResponse("task: %s" % task.title)