from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from serializers import *
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def get(request, value):
    #return HttpResponse("This is {}".format(value))
    context = {'value':value}
    return render(request, "rest_app/index.html", context)

class ZipList(generics.ListAPIView):
    queryset = Zip.objects.all()
    serializer_class = ZipSerializer

class ZipDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zip.objects.all()
    serializer_class = ZipSerializer