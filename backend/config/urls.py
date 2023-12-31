"""bot URL Configuration

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
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # as_view() - means that we refer to it as a normal BestView
    # issuing a random word
    path('random/', views.RandomWord.as_view()),
    path('next/<int:pk>', views.NextWord.as_view()), # <int:pk> - id current word
    # Requests are sent from 0 to 3, if more than 4 - HttpResponseNotFound(...next/0)
]

