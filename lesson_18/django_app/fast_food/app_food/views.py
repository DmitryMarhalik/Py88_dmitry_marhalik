from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<div align='center'>\
                           <h1>Главная страница</h1> \
                        </div>\
                        <h4><a href='/about'><=Go about</a></h4>")

def about(request):
    return HttpResponse('<h1>Страница about</h1>')

def product(request):
    return HttpResponse('<h1>Страница products</h1>')


# Create your views here.
