from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('cars0',views.cars0),
    path('registration',views.registration),
    path('forgotpassword',views.forgotpassword),
    path('regi',views.regi),
    path('logincheck',views.logincheck ),
    path('home1',views.home1),
    path('about1',views.about1),
    path('contact1',views.contact1),
    path('profile',views.profile),
    path('cars1',views.cars1),
    path('logout',views.logout),
    path('confirmcar',views.confirmcar),
    path('confirmcar1',views.confirmcar1),
    path('success2',views.success2),
    path('booked',views.booked),
    path('delete',views.delete),
    path('addcard',views.addcard),
    path('sendmail',views.sendmail),
    

]