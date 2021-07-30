import json
from django.http.response import HttpResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serilizer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serilizer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serilizer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serilizer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serilizer=StudentSerializer(data=python_data)
        if serilizer.is_valid():
            serilizer.save()
            res={'msg':'data created successfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_data,content_type='application/json')


    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serilizer=StudentSerializer(stu,data=python_data,partial=True)#remove partial = True if total update this is required in case of partial update only
        if serilizer.is_valid():
            serilizer.save()
            res={'msg':'data updated successfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted successfully'}
        # json_data=JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)

