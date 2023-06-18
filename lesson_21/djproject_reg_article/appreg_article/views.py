from django.views import View
from .models import Article
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class StartPage(View):
    def get(self, request, *args, **kwargs):
        art = Article.objects.count()
        count = {'count': art}
        return render(request, "users/index.html", context=count)


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


class Create(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'users/create.html')

    @staticmethod
    def post(request, *args, **kwargs):
        art = Article()
        art.author_id = request.user.id
        # art.author_id = user[(len(user) - 1)].id
        art.header = request.POST.get('article-header')
        art.content = request.POST.get('article-content')
        art.save()
        return render(request, 'users/successfully.html')


# def create(request):
#     if request.method == 'GET':
#         return render(request, 'users/create.html')
#
#
#     elif request.method == 'POST':
#         # user = User.objects.all()
#         # print(request.user,request.user.id)
#         # user=User.objects.all().last()
#         # d = User.objects.values('id', 'username')
#         art = Article()
#         art.author_id = request.user.id
#         # art.author_id = user[(len(user) - 1)].id
#         art.header = request.POST.get('article-header')
#         art.content = request.POST.get('article-content')
#         art.save()
#         return render(request, 'users/successfully.html')
