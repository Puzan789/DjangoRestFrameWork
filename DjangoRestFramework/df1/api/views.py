from django.shortcuts import render, HttpResponse
from .models import student
from .serializers import studentser
from rest_framework.renderers import JSONRenderer


def sts(request):
    sts = student.objects.get(id=1)
    serializer = studentser(sts)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")


def stsp(request):
    sts = student.objects.all()
    serializer = studentser(sts, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")
