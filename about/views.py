from django.shortcuts import render
from about.models import AboutMe


# Create your views here.
def about(request):
    # Query to DB to return info about me
    about_me = AboutMe.objects.all()[0]
    return render(request, 'about/about.html', {"about": about_me})
