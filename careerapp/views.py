from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def info(request):
    return render(request,'info.html')
def Inter(request):
    return render(request,'inter.html')
def Diploma(request):
    return render(request,'diploma.html')
def IIIT(request):
    return render(request,'IIIT.html')
def ITI(request):
    return render(request,'ITI.html')
def Vocational(request):
    return render(request,'Vocational.html')
def Travel(request):
    return render(request,'travel.html')
def Sports(request):
    return render(request,'sports.html')
def Govt_jobs(request):
    return render(request,'jobs.html')
def SKills(request):
    return render(request,'skills.html')
def details(request):
    return render(request,'details.html')
def bank_details(request):
    return render(request,'bank-details.html')
def donations(request):
    return render(request,'donations.html')

