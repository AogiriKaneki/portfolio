from django.shortcuts import render
from .models import Job

def home(request):
    joblist = Job.objects
    return render(request,'jobs/home.html',{'jobs':joblist})