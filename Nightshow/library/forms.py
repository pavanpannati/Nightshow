from django.forms import ModelForm 
from library.models import register,login
from .validators import *
from django.forms import *
from django.contrib.auth import authenticate
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect

class Home_forms(ModelForm):
    email=EmailField(label='Email Address',widget=EmailInput({'Placeholder':'ott@nightshow.in'}))
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
    
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')  
        confirm_password=cleaned_data.get('password1')
        if password and confirm_password:
            if password!=confirm_password:
                raise ValidationError('Both Password do not match')
    
class register2_forms(Form):
    otp1=IntegerField(widget=NumberInput(attrs={'placeholder':'0','oninput':"next_field(this,'id_otp2')",'class':'otp-input'}))
    otp2=IntegerField(widget=NumberInput(attrs={'placeholder':'0','oninput':"next_field(this,'id_otp3')",'class':'otp-input'}))
    otp3=IntegerField(widget=NumberInput(attrs={'placeholder':'0','oninput':"next_field(this,'id_otp4')",'class':'otp-input'}))
    otp4=IntegerField(widget=NumberInput(attrs={'placeholder':'0','oninput':"next_field(this,'id_otp5')",'class':'otp-input'}))
    otp5=IntegerField(widget=NumberInput(attrs={'placeholder':'0','oninput':"next_field(this,'id_otp6')",'class':'otp-input'}))
    otp6=IntegerField(widget=NumberInput(attrs={'placeholder':'0','oninput':"next_field(this,'')",'class':'otp-input'}))
    

class login_forms(Form):
    email=EmailField(label='Email Address',widget=EmailInput)
    password=CharField(label='Password',widget=PasswordInput)
    class Meta:
        model=login
        fields='__all__'

    
    