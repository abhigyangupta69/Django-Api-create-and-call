"""ApiProject URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from ApiApplication import views

##############Create Api using ModelViewSet import Router#############
from rest_framework import routers

router=routers.DefaultRouter()
router.register('student',views.StudentViewSet)
########################################

urlpatterns = [
    path('admin/', admin.site.urls),
##############Create Api using ApiView#############
    url("book/",views.BookApiView.as_view()),
####################ModelViewSEt#################
    path('',include(router.urls))
]
