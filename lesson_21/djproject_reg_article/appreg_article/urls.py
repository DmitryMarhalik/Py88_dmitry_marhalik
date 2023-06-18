from django.urls import path
from .views import  StartPage, SignUp, Create

urlpatterns = [
    path('index/', StartPage.as_view(),name='index'),
    path('create/', Create.as_view(), name='create and reg'),
    path("signup/", SignUp.as_view(),name="signup"),
]
