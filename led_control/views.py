from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def on(request):
    return render(request,"on.html")

def off(request):
    return render(request, "index.html")