from django.shortcuts import render
from django.views import View


class HelloView(View):
    def get(self, request, *args, **kwargs):
        data = {
            "text": "Hello",
            "color": "red"
        }
        return render(
            request,
            "startpage.html",
            context=data
        )


class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        data = {
            "text": "Hello World",
            "color": "blue"
        }
        return render(
            request,
            "startpage.html",
            context=data
        )
