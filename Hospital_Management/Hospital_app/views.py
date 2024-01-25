from django.shortcuts import render
from .models import  Hospital_table
# Create your views here.

def Hospital(request):
    return render(request,"Hospital.html")

def Department(request):
    return render(request,"Department.html")

def doctors(request):
    obj1=Hospital_table.objects.all()
    return render(request,'doctors.html',{'doct_list':obj1})

def About(request):
    return render(request,"About.html")

def Contact(request):
    return render(request,"Contact.html")

def booking(request):
    return render(request,"booking.html")


    







