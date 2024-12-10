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
    movie=FileField(upload_to='movie',max_length=None,null=True,blank=True)
    image=ImageField(null=True,upload_to='image' )
    posters=ImageField(null=True,upload_to='posters')
    description=CharField(max_length=1000,default='describe')
    year=CharField(max_length=50,default='2024')
    categories=CharField(max_length=50,default='movie')
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("movie", kwargs={"pk": self.pk})
    