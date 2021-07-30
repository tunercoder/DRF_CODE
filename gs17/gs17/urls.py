from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()# this line creates a default router object

router.register('studentapi', views.StudentViewSet, basename='student')# this line registers our viewset with router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),#This line API urls are determined automatically buy the router
        
]