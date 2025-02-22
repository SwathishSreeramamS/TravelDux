from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request,'registrations/login.html')

def signupPage(request):
    return render(request,'registrations/signup.html')