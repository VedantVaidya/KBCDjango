from django.urls import path
from . import views as v

urlpatterns=[
    path('',v.index),
    path('home',v.home),
    path('play',v.play),
    path('transfer',v.transfer),
    path('transferkbc',v.transferkbc),
    path('transferbp',v.transferbp),
    path('transferconfirm',v.transferconfirm)
]