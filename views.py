from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h1>This is Django project</h1>")

def sample(request):
    return render(request,"sample.html")

def third(request):
    return render(request,'third.html',context={'data':'Ashok'})

def fourth(request):
    fruits=['apple','banana','grapes']
    return render(request,'fourth.html', context={'fruits':fruits})
def url_data(request,name):
    return HttpResponse('<h1>{}</h1>'.format(name))

def ab(request,ab):
    a=ab.split(" ")
    sum=int(a[0])+int(a[1])
    return HttpResponse(str(sum))
def sum(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def great(request,a,b):
    if int(a) > int(b):
        great= str(a) + ' is greater'
    else:
        great=str(b) + ' is greater'
    return HttpResponse(great)

