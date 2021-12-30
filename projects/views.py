from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.
def all_projects(request):
    # fetch all the projects in the database
    projects = Project.objects.all()
    return render(request, "projects/index.html", {"projects":projects})