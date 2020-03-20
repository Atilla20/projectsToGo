from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Projects
from django.http import HttpResponse
from .forms import ProjectsForm


def index(request):
    all_projects = Projects.objects
    return render(request, "templates/index.html", {'all_projects': all_projects})

def createProject(request):
    
    form = ProjectsForm()
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/toGo/')
    context = {'form': form}
    return render(request, 'templates/create.html', context)

def updateProject(request, pk):

    project = Projects.objects.get(id=pk)
    form = ProjectsForm(instance=project)

    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/toGo/')

    context = {'form': form}
    return render(request, 'templates/create.html', context)

def deleteProject(request, pk):
    project = Projects.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/toGo/')

    context = {'item':project}
    return render(request, 'templates/delete.html', context)




        


