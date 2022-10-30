
from django.urls import path
from .views import *
urlpatterns = [   
    path("",home,name="home"),
    path("on",on,name="on"),
    path("off",off,name="off")
]