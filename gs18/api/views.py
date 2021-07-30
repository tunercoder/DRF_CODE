from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudenReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
		"""
		A simple ViewSet for viewing students means list and retrieve will work update delete create will not be avaialable.
		"""
		queryset = Student.objects.all()
		serializer_class = StudentSerializer
			