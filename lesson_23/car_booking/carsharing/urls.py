from django.urls import path
from .views import main_page, create_user, create_car, book_or_take

urlpatterns = [
    path('', main_page,name='main'),
    path('user/', create_user,name='user'),
    path('car/', create_car,name='car'),
    path('book_or_take/', book_or_take,name='book-or-take')
]
