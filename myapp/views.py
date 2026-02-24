from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello_world(request, id):
    print(id)
    return HttpResponse("<h1>Hello %s</h1>" % id)

def about(request):
    return HttpResponse("<h2>About Page</h2>")