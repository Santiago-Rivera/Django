from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def about(request):
    return HttpResponse("<h2>About Page</h2><p>This is the about page of our Django application.</p>")