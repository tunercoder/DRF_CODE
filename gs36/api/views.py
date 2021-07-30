from rest_framework.generics import ListAPIView    
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        filter_backends = [OrderingFilter] #used when per view OrderingFilter filter is used.
        ordering_fields = ['name','roll'] #name or roll no base sorting. http://127.0.0.1:8000/studentapi/?ordering=-roll
        ordering = ['name']