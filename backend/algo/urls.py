"""admin URL Configuration

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
from common.views import Connetion
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from django.contrib import admin
from member.views import Auth

router = routers.DefaultRouter()

urlpatterns = [
    path('connection', Connetion.as_view()),
    path('board', include('board.urls')),
    url(r'^member', Auth.as_view()),

]
