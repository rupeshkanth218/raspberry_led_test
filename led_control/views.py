from django.shortcuts import render,redirect
from .models import LED_STATUS

def home(request):
    obj=LED_STATUS.objects.get(pk=1)
    data={"text":obj.status}
    return render(request,"index.html",data)

def on(request):
    obj=LED_STATUS.objects.get(pk=1)
    obj.status="ON"
    obj.save()
    
    return redirect("home")

def off(request):
    obj=LED_STATUS.objects.get(pk=1)
    obj.status="OFF"
    obj.save()
    
    return redirect("home")