from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(resquest):
    return HttpResponse("Hello world, you're at the polls index.")