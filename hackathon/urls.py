"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from user_login import views
from client_login import views
from hackathon import settings
from django.conf.urls import url,include

urlpatterns = [
	  url(r'^$',views.index,name='index'),
	url(r'^homepage/',views.homepage,name='home'),
    path('admin/', admin.site.urls),
    url(r'^user_login/',include('user_login.urls'),name="login"),
    url(r'^client_login/',include('client_login.urls'),name="clientLogin"),
    url(r'^$',views.user_logout,name="logout"),
    url(r'^special/',views.special, name="special")

    
]


