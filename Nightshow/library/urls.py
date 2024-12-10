from django.urls import path
from .views import Home_view,register1_view,register2_view,login_view,nightshow_view,ImageuploadView,Movie_view,bin_image,forget_password

urlpatterns = [
    path('in/',Home_view,name='home'),
    path('register/',register1_view,name='register1'),
    path('in/register/',register2_view,name='register2'),
    path('login/',login_view,name='login'),
    path('image',ImageuploadView.as_view(),name='image'),
    path('login/main/',nightshow_view.as_view(),name='nightshow'),
    path('login/main1/<int:image_id>/',bin_image,name='bin_image'),
    path('login/main/<int:pk>',Movie_view.as_view(),name='movie'),
    path('login/forget_password',forget_password,name='forget_password')
]
