from rest_framework.generics import  ListCreateAPIView,RetrieveUpdateDestroyAPIView    
from .serializers import StudentSerializer
from .models import Student

# TO list and create:
	
class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    
# TO retrieve update and delete:

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
