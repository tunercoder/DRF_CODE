import json
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from .serializers import StudentSerializer
from .models import Student


#single student data by serializing model student

def student_detail(request,pk):
    stu= Student.objects.get(id=pk)
    # print(stu)
    serializer=StudentSerializer(stu)
    # print(serializer)
    print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)


#all student data by serializing queryset

def student_list(request):
    stu= Student.objects.all()
    # print(stu)
    serializer=StudentSerializer(stu,many=True)
    # print(serializer)
    print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json') instead of these 2 lines we use JsonResponse

    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        print(json_data)
        stream = io.BytesIO(json_data) #reading json
        pythondata=JSONParser().parse(stream) #parsing streamed json data to python native  dataype
        print(pythondata)
        serializer=StudentSerializer(data=pythondata) #calling deserialization means creating complex data that is a validate_data dictionary python
        if serializer.is_valid():#checking if complex data is valid or not 
            serializer.save() #saving complex data object to database
            res={'msg':'created successfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json') 