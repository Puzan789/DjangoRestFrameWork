from django.shortcuts import render, HttpResponse
from .models import stumodel
from .serializers import serializerst
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# Create your views here.
def show(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = serializerst(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "done created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
    else:
        json_data - JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
