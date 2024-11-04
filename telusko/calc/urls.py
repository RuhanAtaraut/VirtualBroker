from django.urls import path
from  . import  views


urlpatterns = [
   
    path('login/', views.login, name='login'),
    path('log', views.log, name='log'),
    path('addrooms', views.addrooms, name='addrooms'),
    path('addmess', views.addmess, name='addmess'),
    path('otp/', views.mail_send, name ='mail_send'),
    path('otp_check', views.otp_check, name='otp_check'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('register',views.register,name='register'),
    path('', views.index, name='index'),
    #path('add', views.add, name='add'),
    #path('add1', views.add1, name='add1'),
    #path('add2', views.add2, name='add2'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('fetch', views.fetch, name='fetch'),
    path('fetch1', views.fetch1, name='fetch1'),
    path('fill', views.fill, name='fill'),
    path('fill1', views.fill1, name='fill1'),
    path('fill2', views.fill2, name='fill2'),
    path('submit', views.submit, name='submit'),
    path('submit1', views.submit1, name='submit1'),

    path('load_courses/', views.load_courses, name='load_courses'),
    path('load_courses1/', views.load_courses1, name='load_courses1'),
]