from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,logout
from library.backends import LoginBackend
from django.contrib import messages
from .models import register,movie_posters
from .forms import Home_forms,register1_forms,register2_forms,login_forms
from .validators import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import movie_posters_serializers

def Home_view(request):
    allimages=movie_posters.objects.all()
    if request.method=='POST':
        form=Home_forms(request.POST)
        email=request.POST.get('email')
        request.session['email_session']=email
        if register.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists. Please login.')
            return redirect('login')
        if form.is_valid():
            return redirect('register1')
        
    else:
        form=Home_forms()
    return render(request,'library/home.html',{'form':form,'images':allimages})

def register1_view(request):
    if request.method=='POST':
        form=register1_forms(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=request.session.get('email_session',None)
            recipient=form.cleaned_data['email']
            request.session['mail_session']=recipient
            otp=generete_otp()
            vef_code_for_registration(otp,name,recipient)
            request.session['otp']=otp
            # messages.add_message(request,messages.success,'OTP Sent Successfully')
            form.cleaned_data['password']=make_password(form.cleaned_data['password'])
            print(form.cleaned_data['password'])
            data=form.cleaned_data
            print(data)
            request.session['form_data']=data
            return redirect('register2')
    else:
        form=register1_forms()
    return render(request,'library/register1.html',{'form':form})

def register2_view(request):
    mail=request.session.get('mail_session',None)
    if request.method=='POST':
        form=register2_forms(request.POST)
        if form.is_valid():
            otp1=form.cleaned_data['otp1']
            otp2=form.cleaned_data['otp2']
            otp3=form.cleaned_data['otp3']
            otp4=form.cleaned_data['otp4']
            otp5=form.cleaned_data['otp5']
            otp6=form.cleaned_data['otp6']
            OTP=int(str(otp1)+str(otp2)+str(otp3)+str(otp4)+str(otp5)+str(otp6))
            print(OTP,type(OTP))
            if OTP==request.session.get('otp'):
                #messages.add_message(request,messages.success,'OTP validated successfully')
                data=request.session.get('form_data',None)
                data.pop('password1')
                print(data)
                register.objects.create(**data)
                if mail:
                    del request.session['mail_session']
                return redirect('nightshow')
    else:
        form=register2_forms()
    return render(request,'library/register2.html',{'form':form,'mail':mail})

def login_view(request):
    if request.method=='POST':
        form=login_forms(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=LoginBackend.authenticate(email=email,password=password)
            print(user)
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


class nightshow_view(ListView):
    model=movie_posters
    template_name='library/nightshow.html'
    context_object_name='images'
    login_url='/login/'
    redirect_field_name='next'

def bin_image(request,image_id):
    try:
        image_obj=movie_posters.objects.get(id=image_id)
        return HttpResponse(image_obj.posters,content_type='image/jpeg')
    except movie_posters.DoesNotExist:
        return HttpResponse('Image Not Found',status=404)
class Movie_view(DetailView):
    model=movie_posters
    template_name='library/movie.html'
    context_object_name='images'
    
class ImageuploadView(APIView):
    def post(self,request,*args,**kwrgs):
        serializer=movie_posters_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'image uploaded successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
def forget_password(request):
    pass

def logout_view(request):
    logout(request)
    messages.success(request,'You has successfull logged out')
    return redirect('home')