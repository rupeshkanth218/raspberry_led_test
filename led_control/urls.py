
from django.urls import path
from .views import *
urlpatterns = [   
    path("",home,name="home"),
    path("on",on,name="ON"),
    path("off",off,name="OFF")
]