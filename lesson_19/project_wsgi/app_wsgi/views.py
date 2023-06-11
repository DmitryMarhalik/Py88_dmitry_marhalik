from django.shortcuts import render
from django.views import View


def hello(request):
    data = {
        "text": "Hello",
        "color": "red"
    }
    return render(request, "startpage.html", context=data)


def helloworld(request):
    data = {
        "text": "Hello World",
        "color": "blue"
    }
    return render(request, "startpage.html",context=data)
