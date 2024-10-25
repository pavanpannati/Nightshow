from django.forms import ModelForm 
from library.models import register,login
from .validators import *
from django.forms import *
from django.contrib.auth import authenticate
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect



class Home_forms(ModelForm):
    email=EmailField(label='Email Address')
    class Meta:
        model=register
        fields=['email']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if register.objects.filter(email=email).exists():
            raise ValidationError("The User with Email already exists.")       
        return email
    
class register1_forms(ModelForm):
    name=CharField(label='Full Name')
    email=EmailField(label='Email Address',widget=EmailInput)
    username=CharField(label='Username')
    #mobile=PhoneNumberField(label='Mobile Number',region='IN')
    password=CharField(label='Password',help_text='Your Password must be atleast 8 characters,Strong Password',widget=PasswordInput)
    password1=CharField(label='Confirm Password',help_text='Enter the Same Password as Before',widget=PasswordInput)
    class Meta:
        model=register
        fields=['name','email','username','password']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if register.objects.filter(email=email).exists():
            raise ValidationError("The User with Email already exists.")        
        return email
    
    def clean_user(self):
        user1 = self.cleaned_data.get('username')
        if register.objects.filter(username=user1).exists():
            raise ValidationError("Username is not supported")   
        return user1   
class register2_forms(Form):
    otp=IntegerField(label="One Time Password")
    
# class nightshow_form(Form):
#     a
class login_forms(Form):
    email=EmailField(label='Email Address',widget=EmailInput)
    password=CharField(label='Password',widget=PasswordInput)
    class Meta:
        model=login
        fields='__all__'
   

    
    