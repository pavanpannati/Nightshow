#import name,email,otp
from random import randint
from django.core.mail import send_mail
from django.shortcuts import render
from .models import register
from django.forms import ValidationError
from django.core.exceptions import ValidationError
def generete_otp():
    otp=randint(10**5,10**6)
    return otp
def vef_code_for_registration(otp,fname,recipient):
    subject='Verification Code for Registration'
    content=f'''Dear {fname},
    Your 6 digit otp to register Nightshow OTT account is {otp}.
    In case you have not requested to OTP, Ignore or contact Nightshow support team
    We kindly request not to share the otp with anyone. 
    
    Thanks,
    Nightshow OTT'''
    send_mail(subject,content,'pavanpannati5@gmail.com',[recipient])

def vef_code_for_login(fname,otp):
    subject='One Time Code for Login'
    content=f'''Dear {fname},
    One Time Password (OTP) to verify your email is {otp}
    In case you have not requested to OTP, Ignore or contact Nightshow support team
    
    Thanks,
    Nightshow OTT'''
    
def vef_code_for_reset(fname,otp):
    subject='Password Reset'
    content=f'''Dear {fname}
    You requested to reset the password for your Nightshow account
    The requested OTP is {otp}. 
    In case you have not requested to OTP, Ignore or contact Nightshow support team
    If you did not request a passwoord reset, please ignore this email or reply to us. 
    
    Thanks,
    Nightshow'''

def suc_reg(fname,recipient):
    subject='Successful registration for your Nightshow account'
    content=f'''Dear {fname}
    You are Successfully registered into Nightshow-OTT account and you won your free membership. valid for a month
    
    Thanks,
    Nightshow'''
    send_mail(subject,content,'pavanpannati5@gmail.com',[recipient])
    

