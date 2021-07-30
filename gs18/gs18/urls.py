from django.contrib import admin
from django.urls import path,include
import rest_framework
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()# this line creates a default router object

router.register('studentapi', views.StudentModelViewSet, basename='student')# this line registers our viewset with router
router.register('studentapiro',views.StudenReadOnlyViewSet, basename='studentro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),#This line API urls are determined automatically buy the router
      
]