from django.shortcuts import render
from .forms import AutoForm, UserForm, BookTakeForm
from .models import Auto
# from rest_framework.generics import GenericAPIView,ListAPIView
# from .serializers import AutoSerializer
# from rest_framework.filters import SearchFilter
#
# class MainView(ListAPIView):
#     queryset=Auto.objects.all()
#     serializer_class = AutoSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['vin_code']
#


def main_page(request):
    auto = Auto.objects.filter(status__in=['taken', 'booked']).order_by('id')
    dict = {"auto": auto}
    return render(request, 'main.html', context=dict)


def create_user(request):
    if request.method == 'GET':
        user_form = UserForm()
        return render(request, 'create_user.html', context={'form': user_form})

    elif request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            error = None
            user_form.save()
        else:
            error = "Error input!!!"
        return render(request, 'create_user.html', context={'success_message': 'Success!', 'error': error})


def create_car(request):
    if request.method == 'GET':
        auto_form = AutoForm()
        return render(request, 'create_car.html', context={'form': auto_form})

    elif request.method == 'POST':
        error = None
        auto_form = AutoForm(request.POST)
        if auto_form.is_valid():
            auto_form.save()
        else:
            error = auto_form.errors
        return render(request, 'create_car.html', context={'success_message': 'Success!', 'error': error})


def book_or_take(request):
    if request.method == 'GET':
        book_or_take_form = BookTakeForm()
        return render(request, 'book_or_take.html', context={'form': book_or_take_form})

    elif request.method == 'POST':
        # book_or_take_form = BookTakeForm()
        vin = request.POST['vin_code']
        automodel_id = request.POST['auto_model']
        userid = request.POST['user']
        autostatus = request.POST['status']
        check = Auto.objects.filter(auto_model=automodel_id).filter(vin_code=vin) \
            .update(user_id=userid, status=autostatus)
        if (autostatus == 'free' and not userid) or ((autostatus in ['booked', 'taken']) and userid):
            if check:
                return render(request, 'book_or_take.html', context={'succ_message': 'Success update!'})
            else:
                return render(request, 'book_or_take.html', context={'message': 'Error! Vin does not correspond auto'})
        else:
            return render(request, 'book_or_take.html', context={'message': 'Error input!'})
