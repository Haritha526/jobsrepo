from django.shortcuts import render
from jobsapp.models import HydJobs
from jobsapp.models import PuneJobs
from jobsapp.models import BngJobs
# Create your views here.
def homepage_view(request):
    return render(request,'jobsapp/index.html')
def hydjobs_view(request):
    hydjobslist1 = HydJobs.objects.all()
    mydict = {'hydjobslist':hydjobslist1}
    return render(request,'jobsapp/alljobs.html',mydict)

def punejobs_view(request):
    punejobslist = PuneJobs.objects.all()
    mydict1 = {'punejobslist':punejobslist}
    return render(request,'jobsapp/alljobs.html',mydict1)

def bngjobs_view(request):
    bngjobslist = BngJobs.objects.all()
    mydict2 = {'bngjobslist':bngjobslist}
    return render(request,'jobsapp/alljobs.html',mydict2)