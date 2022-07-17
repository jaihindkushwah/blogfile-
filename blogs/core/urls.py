
from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('blog_page',views.blog_page,name='blog_page'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('forget',views.forget,name='forget'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
#    path('ind', views.ind, name ='ind'),


]
