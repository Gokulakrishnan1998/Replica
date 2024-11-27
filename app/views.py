from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from app import forms
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.models import User
from .models import *

# Create your views here.

# homepage
def homepage(request):
    return render(request,'homepage/homepage.html')

# Admin signup
def admin_signup(request):
    if request.method == 'GET':
        return render(request,'signup/adminsignup.html',{'admin_signup':forms.signupPage})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if not username and password and re_password and email and phone:
            return HttpResponse('Please enter all details to sign up')
        
        if password != re_password:
            return render(request,'signup/adminsignup.html',{'admin_signup':forms.signupPage,'status':'Password Mismatched'})
            

        
        if User.objects.filter(username = username).exists():
            return HttpResponse(f'{username} Already exists')
        else:
            # Admin creation
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
                id=phone,
            )
            return HttpResponse('admin signup successful')

# Employee signup
def signup_page(request):
    if request.method == 'GET':
        return render(request,'signup/empsignup.html',{'signup_form':forms.signupPage})
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        print(username,password,re_password,email,phone)

        if not username and password and re_password and email and phone:
            return HttpResponse('Please enter all details to sign up')
        
        if password != re_password:
            return render(request,'signup/empsignup.html','Password Mismatch')
        
        if Signup.objects.filter(username = username).exists():
            return HttpResponse(f'{username} Already exists')
        else:
            Signup.objects.create(
                username=username,
                password=password,
                re_password=re_password,
                email=email,
                phone=phone)

            return HttpResponse('Employee signup successfully')

# Login page

def user_login(request):
    if request.method == 'GET':
        return render(request,'signup/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #If admin login
        if User.objects.filter(username=username):
            user = authenticate(request=request,username=username,password=password)
            login(request,user)
            return redirect('list')
        
        # If employee login
        elif Signup.objects.filter(username=username):
            return HttpResponse('Employee logged In')
        else:
            return render(request,'signup/login.html',{'status':'Please enter correct Username/password'})
        


