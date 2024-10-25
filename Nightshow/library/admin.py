from django.contrib import admin
from .models import register,login,movie_posters
# Register your models here.
class register_admin(admin.ModelAdmin):
    list_display=['name','email','password','mobile']
admin.site.register(register,register_admin)
class movie_posters_admin(admin.ModelAdmin):
    list_display=['pk','movie','title','posters']
admin.site.register(movie_posters,movie_posters_admin)
admin.site.register(login)