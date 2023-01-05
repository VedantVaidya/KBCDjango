from django.urls import path
from . import views as v

urlpatterns=[
    path('login',v.handellogin,name='login'),
    path('logout',v.handellogout,name='logout'),
    path('signup',v.handelsignup,name='signup'),
]