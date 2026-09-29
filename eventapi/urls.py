"""
URL configuration for eventapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from eventhub.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()

router.register('register',SignUpViewSet,basename="register")
router.register('booking',BookingModelViewSet,basename="booking")
router.register('event',EventViewSet,basename="event")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',obtain_auth_token),
    path('history/',BookingHistory.as_view())
]+router.urls
