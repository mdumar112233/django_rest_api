from django.http import JsonResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import De_Serializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def createpost(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = De_Serializer(data = pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data create'}
            return JsonResponse(res)
            
        return JsonResponse(serializer.errors)