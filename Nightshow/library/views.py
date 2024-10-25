from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from library.backends import LoginBackend
from django.core.mail import send_mail
from django.contrib import messages
from .models import register,movie_posters
from .forms import Home_forms,register1_forms,register2_forms,login_forms
from .validators import *
from django.http import HttpResponse

def Home_view(request):
    allimages=movie_posters.objects.all()
    if request.method=='POST':
        form=Home_forms(request.POST)
        email=request.POST.get('email')
        if register.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists. Please login.')
            return redirect('login')
        if form.is_valid():
            return redirect('register1')
        
    else:
        form=Home_forms()
    return render(request,'library/base.html',{'form':form,'images':allimages})

def register1_view(request):
    if request.method=='POST':
        form=register1_forms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            recipient=form.cleaned_data['email']
            otp=generete_otp()
            vef_code_for_registration(otp,name,recipient)
            request.session['otp']=otp
            # messages.add_message(request,messages.success,'OTP Sent Successfully')
            global data
            data=form.save(commit=False)
            data.set_password(form.cleaned_data['password'])
            data.is_active=True
            return redirect('register2')
    else:
        form=register1_forms()
    return render(request,'library/register1.html',{'form':form})

def register2_view(request):
    if request.method=='POST':
        form=register2_forms(request.POST)
        if form.is_valid():
            otp2=form.cleaned_data['otp']
            if otp2==request.session.get('otp'):
                #messages.add_message(request,messages.success,'OTP validated successfully')
                data.save()
                return redirect('home')
            else:
                raise ValidationError('Invalid OTP, Please try again')
    else:
        form=register2_forms()
    return render(request,'library/register2.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=login_forms(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            email='pavanpannati8@gmail.com'
            password='pavan'
            user=LoginBackend.authenticate(email=email,password=password)
            if user is not None:
                # request.session['user_id']=user.id
                login(request,user,backend='library.backends.LoginBackend')
                if user.is_superuser:
                    return redirect('/admin')
                messages.success(request,"Login Successful")
                return redirect('main/')
            else:
                messages.error(request,'Invalid, Username or Password')
    else:
        form=login_forms()
    return render(request,'library/login.html',{'form':form})

@login_required
def nightshow_view(request):
    images=movie_posters.objects.all()
    return render(request,'library/home.html',{'images':images})

def subscribe(request):
    return render(request,'library/subscribe.html')