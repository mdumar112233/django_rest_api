from functools import partial
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentCreateSerializer
from .models import Studentcrud
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

## SINGLE AND MULTIPLE DATA READ FROM DATABASE
@csrf_exempt
def student_api(request):

    ### GET REQUEST
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        print('user request id', pythondata)

        id = pythondata.get('id', None)
        print('id', id)

        ### WITH ID SINGLE DATA GET FROM DATABASE
        if id is not None:
            stu = Studentcrud.objects.get(pk=id)
            serializer = StudentCreateSerializer(stu)

            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        ### WITHOUT ID ALL DATA GET FROM DATABASE
        stu = Studentcrud.objects.all()
        serializer = StudentCreateSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    ### POST REQUEST
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentCreateSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data create'}
            response = JSONRenderer().render(res)
            return HttpResponse(response, content_type= 'application/json')

        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response, content_type= 'application/json')
        

    ### UPDATE REQUEST
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        print('pythondata', pythondata)

        id = pythondata.get('id')
        stu = Studentcrud.objects.get(pk=id)

        serializer = StudentCreateSerializer(stu, data= pythondata, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            return JsonResponse(res)
        
        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response, content_type='application/json')

    ### DELETE  METHOD
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        id = pythondata.get('id')
        stu = Studentcrud.objects.get(pk=id)
        stu.delete()

        res = {'msg': 'data delete'}
        return JsonResponse(res)
    
    return HttpResponse('data is not delete')


  






