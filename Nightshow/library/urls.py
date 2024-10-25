from django.urls import path
from .views import Home_view,register1_view,register2_view,login_view,nightshow_view

urlpatterns = [
    path('in/',Home_view,name='home'),
    path('register/',register1_view,name='register1'),
    path('in/register/',register2_view,name='register2'),
    path('login/',login_view,name='login'),
    path('login/main/',nightshow_view,name='nightshow'),
    
]
