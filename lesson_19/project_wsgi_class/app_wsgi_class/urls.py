from django.urls import path
from .views import HelloView, HelloWorldView

urlpatterns = [
    path('hello/', HelloView.as_view()),
    path('hello/world/', HelloWorldView.as_view()),
]