from rest_framework.generics import ListAPIView    
from .serializers import StudentSerializer
from .models import Student
from .mypagination import MyPageNumberPagination

class StudentList(ListAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer
        pagination_class = MyPageNumberPagination

        