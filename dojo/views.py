# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.rstrip('/').split('/')))
    return HttpResponse(result)
    # numbers = '1/2/3/4/5/6 ...'
    #request: HttpRequest

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))
