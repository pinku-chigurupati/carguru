"""CARGURU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('login',include('app.urls')),
    path('home',include('app.urls')),
    path('contact',include('app.urls')),
    path('cars0',include('app.urls')),
    path('registration',include('app.urls')),
    path('forgotpassword',include('app.urls')),
    path('regi',include('app.urls')),
    path('logincheck',include('app.urls')),
    path('home1',include('app.urls')),
    path('about1',include('app.urls')),
    path('contact1',include('app.urls')),
    path('profile',include('app.urls')),
    path('cars1',include('app.urls')),
    path('logout',include('app.urls')),
    path('confirmcar',include('app.urls')),
    path('confirmcar1',include('app.urls')),
    path('success2',include('app.urls')),
    path('booked',include('app.urls')),
    path('delete',include('app.urls')),
    path('addcard',include('app.urls')),
    path('addcard1',include('app.urls')),
    path('sendmail',include('app.urls')),
   

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

