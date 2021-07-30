from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,\
    RetrieveUpdateAPIView,RetrieveDestroyAPIView    
from .serializers import StudentSerializer
from .models import Student
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        throttle_classes=[ScopedRateThrottle]
        throttle_scope = 'view_throttle'


class StudentCreate(CreateAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        throttle_classes=[ScopedRateThrottle]
        throttle_scope = 'create_throttle'


class StudentRetrieve(RetrieveAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        throttle_classes=[ScopedRateThrottle]
        throttle_scope = 'view_throttle'


class StudentUpdate(UpdateAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        throttle_classes=[ScopedRateThrottle]
        throttle_scope = 'create_throttle'


class StudentDelete(DestroyAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        throttle_classes=[ScopedRateThrottle]
        throttle_scope = 'create_throttle'


