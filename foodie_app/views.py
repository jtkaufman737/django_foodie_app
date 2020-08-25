from django.shortcuts import render
from django.http import HttpResponse

# create views here 

def index(request):
    return HttpResponse('Hello World')

def item(request):
    return HttpResponse('<h2>This is an item</h2>')
