
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET','POST','PUT', 'PATCH' ,'DELETE'])
def student_api(request, pk=None):
    if request.method=='GET':
        # id=request.data.get('id') this is used when we were not using browsable api for testing
        id=pk #for browsable api use this as parameter from url
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'successfully created'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        # id=request.data.get('id')
        id=pk 
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'successfully updated'}
            return Response(res,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PATCH':
        # id=request.data.get('id')
        id=pk 
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'successfully updated'}
            return Response(res,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        # id=request.data.get('id')
        id=pk 
        stu = Student.objects.get(pk=id)
        stu.delete()
        res={'msg':'data deleted'}
        return Response(res,status=status.HTTP_200_OK)




