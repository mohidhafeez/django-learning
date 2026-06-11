from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.


# def index(request):
#     return HttpResponse('<h1>Hello World</h1>')


def index(request):

    features=Feature.objects.all()
    
    return render(request, 'index.html',{'features':features})


def counter(request):
    text=request.POST['text']
    words=len(text.split())
    return render(request,'counter.html',{
        'amount':words
    })
