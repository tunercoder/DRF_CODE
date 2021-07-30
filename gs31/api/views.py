from rest_framework import viewsets
from rest_framework import throttling
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from .models import Student
from .serializers import StudentSerializer
from .throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
    # throttle_classes=[JackRateThrottle,AnonRateThrottle] used as view wise user throttle to jackratethrottle is fixed in setting