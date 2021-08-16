from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact,User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    context={

    }
    return render(request,'home.html',context)

def contact(request):
    if request.method=="POST":
        First_Name=request.POST.get('fname')
        Service=request.POST.get('service')
        Last_Name=request.POST.get('lname')
        Email=request.POST.get('email')
        Phone=request.POST.get('phone')
        Company=request.POST.get('company')
        Message=request.POST.get('message')
        contact=Contact(First_Name=First_Name,Service=Service,Last_Name=Last_Name,Email=Email,Phone=Phone,Company=Company,Message=Message)
        contact.save()
        return render(request, 'thankyou.html',{
            'First_Name':First_Name,
            'Service':Service
        })
    return render(request,'contact.html')

