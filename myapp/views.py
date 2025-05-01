from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    title = "Django Course!!"
    return render(request,"index.html", {
        'title': title
    })
    #return HttpResponse("Index page")

def about(request):
    usurname = "Andres"
    return render(request,"about.html", {
        'username': usurname
    })
    #return HttpResponse('about')

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html', {
        'projects': projects
    })
    #return JsonResponse(projects, safe=False)

def tasks(request):
    #task = Task.objects.get(title=title)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request,'tasks.html', {
        'tasks': tasks
    })
    #return HttpResponse('tasks: %s' % task.title)
