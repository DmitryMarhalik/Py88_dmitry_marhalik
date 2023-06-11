from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Article


class StartPage(View):
    def get(self, request,*args,**kwargs):
        art = Article.objects.count()
        count = {'count': art}
        return render(request, "index.html",context=count)


def create(request):
    if request.method == 'GET':
        return HttpResponse \
            ('<form action="/create/" method="POST">'
             '<div class="container" align="center">\
                        <textarea name="article-header" placeholder="Введите заголовок" '
             'cols="80" rows="3"></textarea></br>\
               <textarea name="article-content" placeholder="Напишите здесь статью" '
             'cols="80" rows="20"></textarea></br>\
               <button type="submit"><p><font size="4" color="Green" face="Arial">Create!</font></p></button>'
             '</div>\
             </form><a href="/index"><-Go back</a></h4>')

    elif request.method == 'POST':
        art = Article()
        art.header = request.POST.get('article-header')
        art.content = request.POST.get('article-content')
        art.save()
        return HttpResponse('<div align="center">'
                            ' <p><font size="5" color="purple" face="Arial">Text added successfully!</font></p>\
                             </div>\
                             <h4><a href="/create"><-Go back</a></h4>')
