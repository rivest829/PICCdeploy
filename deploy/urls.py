"""deploy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from murong import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^murong/', views.login),
    url(r'^deploy/', views.deploy),
    url(r'^upload/', views.upload),
    url(r'^execute/', views.execute),
    url(r'^dellog/', views.dellog),
    url(r'^touch/', views.touch),
    url(r'^sysInfo/', views.sysInfo),
    url(r'^stepResponse/', views.stepResponse),
    url(r'^stepCallback/', views.stepCallback),
    url(r'^login/', views.login),
    url(r'^greplog/', views.greplog),
    url(r'^backendlogin/', views.backend_login),
    url(r'^resultGreplog/', views.resultGreplog),
    url(r'^backendadmin/', views.backend),
    url(r'^backend/', views.backend),
    url(r'^add_user/', views.add_user),
    url(r'^set_user_permission/', views.set_user_permission),
]
