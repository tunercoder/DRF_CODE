from rest_framework.generics import ListAPIView    
from .serializers import StudentSerializer
from .models import Student

class StudentList(ListAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        