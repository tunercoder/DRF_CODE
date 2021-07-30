from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,\
    RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView    
from .serializers import StudentSerializer
from .models import Student

class StudentList(ListAPIView):
		queryset=Student.objects.all()
		serializer_class=StudentSerializer


class StudentCreate(CreateAPIView):
		queryset=Student.objects.all()
		serializer_class=StudentSerializer


class StudentRetrieve(RetrieveAPIView):
		queryset=Student.objects.all()
		serializer_class=StudentSerializer


class StudentUpdate(UpdateAPIView):
		queryset=Student.objects.all()
		serializer_class=StudentSerializer


class StudentDelete(DestroyAPIView):
		queryset=Student.objects.all()
		serializer_class=StudentSerializer


# TO list and create:
	
class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
		
# TO retrieve and update:
	
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
		
# TO retrieve and delete:

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    
# TO retrieve update and delete:

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
