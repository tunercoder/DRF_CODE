from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        print('******************list*******************')
        print('Basename',self.basename)
        print('Action',self.action)
        print('Detail',self.detail)
        print('Suffix',self.suffix)
        print('Name',self.name)
        print('Description',self.description)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def create(self, request):
        print('******************create*******************')
        print('Basename',self.basename)
        print('Action',self.action)
        print('Detail',self.detail)
        print('Suffix',self.suffix)
        print('Name',self.name)
        print('Description',self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        print('******************Retrieve*******************')
        print('Basename',self.basename)
        print('Action',self.action)
        print('Detail',self.detail)
        print('Suffix',self.suffix)
        print('Name',self.name)
        print('Description',self.description)
        id=pk
        if id is not None:    
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        return Response({'msg':'no id supplied'},status=status.status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):

        print('******************Update*******************')
        print('Basename',self.basename)
        print('Action',self.action)
        print('Detail',self.detail)
        print('Suffix',self.suffix)
        print('Name',self.name)
        print('Description',self.description)

        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None):
        print('******************Partial_update*******************')
        print('Basename',self.basename)
        print('Action',self.action)
        print('Detail',self.detail)
        print('Suffix',self.suffix)
        print('Name',self.name)
        print('Description',self.description)

        id=pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        print('******************destroy*******************')
        print('Basename',self.basename)
        print('Action',self.action)
        print('Detail',self.detail)
        print('Suffix',self.suffix)
        print('Name',self.name)
        print('Description',self.description)

        id=pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':' data deleted'})
