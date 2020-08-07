from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app(request):
    return HttpResponse('<h1>this is django app</h1>')

def base(request):
    return render(request,'base.html')
def child(request):
    return render(request,'myapp/child.html')
def home(request):
    return render(request,'myapp/home.html')
def base1(request):
    return render(request,'base1.html')
def child1(request):
    return render(request,'myapp/child1.html')

def profile(request):
    name="Ashok"
    return render(request,"myapp/profile.html",context={'name':name})
def base2(request):
    return render(request,'base2.html')