"""p11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello/',views.hello,name='hello'),
    #path('sample/',views.sample,name='sample'),
    #path('third/',views.third,name="third"),
    #path('fourth/',views.fourth,name='fourth'),
    #path('url_data/<name>/',views.url_data,name='urldata'),
    #path('ab/<ab>/',views.ab,name='ab'),
    #path('sum/<a>/<b>/',views.sum,name='sum'),
    #path('great/<a>/<b>/',views.great,name="great"),
    path('myapp/',include('myapp.urls')),
    path('base/',views.base,name="base"),
    path('child/',views.child,name="child"),
    path('base1/',views.base1,name="base1"),
    path('child1/',views.child1,name="child1"),
    path('base2/',views.base1,name="base2"),
]
