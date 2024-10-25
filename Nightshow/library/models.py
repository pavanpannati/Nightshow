from django.db import models
from django.db.models import *
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

from datetime import datetime,date
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.
class register(AbstractUser):
    name=CharField(max_length=20)
    email=EmailField(unique=True)
    #email otp field    
    mobile=CharField(max_length=13)
    password=CharField(max_length=90,null=True,blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name','password','username']

class login(models.Model):
    email=EmailField(max_length=50)
    password=CharField('Password',max_length=30)

class movie_posters(models.Model):
    title=CharField(verbose_name='title',max_length=100)
    movie=ImageField( upload_to='images/', height_field=None, width_field=None, max_length=None)
    video=FileField(upload_to='movies/',null=True )
    posters=ImageField(upload_to='images/',null=True)