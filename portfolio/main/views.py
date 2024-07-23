from django.shortcuts import render, get_object_or_404
from .models import Project, Tag

def home(request):
    return render(request, 'home.html', {
        
    })

def contact(request):
    return render(request, 'contact.html', {
        
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project.html', {
        'project': project
    })