from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):
    return render(request, "Index.html",locals())

def about(request):
    return render(request, "About.html",locals())

def education(request):
    allEducation = Education.objects.all()
    return render(request, "Education.html",locals())

def project(request):
    allProject = Project.objects.all()
    return render(request, "Project.html",locals())

def contact(request):
    return render(request, "Contact.html",locals())
