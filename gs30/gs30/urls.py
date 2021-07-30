from django.contrib import admin
from django.urls import path,include
from api import views as api_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router = DefaultRouter()# this line creates a default router object

router.register('studentapi', api_views.StudentModelViewSet, basename='student')# this line registers our viewset with router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),#This line API urls are determined automatically buy the router
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),   
]