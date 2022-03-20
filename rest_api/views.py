from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# MODEL OBJECT - SINGLE STUDENT DATA
def student_detail(request):
    stu = Student.objects.get(pk=1)

    # convert into python data
    serializer = StudentSerializer(stu)
    print(serializer)

    # convert into json data
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)

    return HttpResponse(json_data, content_type='application/json')

# ALL QUERY SET STUDENT DATA
def student_list(request):
    stu = Student.objects.all()

    # convert into python data
    serializer = StudentSerializer(stu, many=True)

    # convert into json data
    # json_data = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data, content_type='application/json')
    
    return JsonResponse(serializer.data, safe=False)









