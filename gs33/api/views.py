from rest_framework.generics import ListAPIView    
from .serializers import StudentSerializer
from .models import Student
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
        queryset=Student.objects.all()
        serializer_class=StudentSerializer


        def get_queryset(self):
                """
                This view should return a list of all the purchases
                for the currently authenticated user.
                """
                user = self.request.user
                return Student.objects.filter(pass_by=user)


