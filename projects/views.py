from django.shortcuts import render
from projects.models import Project


# Create your views here.
def all_projects(request):
    # Query to DB to return all project
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {"projects": projects})
