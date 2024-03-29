"""sitioweb URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from app import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logueado/', views.login, name='logueado'),
    path('logout/', views.logout, name='logout'),
    path('admin/', admin.site.urls),
]