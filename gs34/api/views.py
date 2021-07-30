from rest_framework.generics import ListAPIView    
from .serializers import StudentSerializer
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend

class StudentList(ListAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        filter_backends = [DjangoFilterBackend] #used when per view set filter backend in used.
        filterset_fields = ['name', 'roll']
        

