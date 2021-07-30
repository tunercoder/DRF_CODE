from rest_framework.generics import ListAPIView    
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        filter_backends = [SearchFilter] #used when per view search filter is used.
        # search_fields = ['name', 'city']
        search_fields = ['^name'] #name starts with search. http://127.0.0.1:8000/studentapi/?search=r
        

