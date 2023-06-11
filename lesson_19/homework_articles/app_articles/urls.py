from django.urls import path
from .views import create, StartPage

urlpatterns = [
    path('index/', StartPage.as_view()),
    path('create/', create),
]
