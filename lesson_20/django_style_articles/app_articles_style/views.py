from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Article,Author


class StartPage(View):
    def get(self, request,*args,**kwargs):
        art = Article.objects.count()
        count = {'count': art}
        return render(request, "index.html",context=count)


def create(request):
    if request.method == 'GET':
        return render(request,'create.html')

    elif request.method == 'POST':
        author = Author()
        author.name = request.POST.get('name')
        author.email = request.POST.get('email')
        # aid=Author.objects.get(name="")
        author.save()

        art = Article()
        art.header = request.POST.get('article-header')
        art.content = request.POST.get('article-content')
        art.save()
        return render(request,'successfully.html')
