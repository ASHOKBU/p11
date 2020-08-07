from django.urls import path
app_name='myapp'
from myapp import views

urlpatterns=[
    path('app/',views.app,name='app'),
    path('home/',views.home,name='home'),
    path('profile/',views.profile,name='profile')
]