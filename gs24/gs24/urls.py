from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()# this line creates a default router object

router.register('studentapi', views.StudentModelViewSet, basename='student')# this line registers our viewset with router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),#This line API urls are determined automatically buy the router
    path('auth/',include('rest_framework.urls',
    namespace='rest_framework')),#using session authentication so login and logout urls must be included
          
]