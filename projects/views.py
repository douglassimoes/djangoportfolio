from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.
def all_projects(request):
    # fetch all the projects in the database
    projects = Project.objects.all()
    return render(request, "projects/index.html", {"projects":projects})

# pk is been passed by parameter/argument from urls
def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render( request, "projects/detail.html", {"project":project})