from django.shortcuts import render
from .models import User, AutoModel, Auto, Brand


def main_page(request):
    auto = Auto.objects.all()
    return render(request, 'main.html', {"auto": auto})


# return render(request,'main.html',context={'title':'Главная страница'})


def create_user(request):
    if request.method == 'GET':
        # return render(request,'create_user.html', {'title':'Создание юзера'})
        return render(request, 'create_user.html')
    elif request.method == 'POST':
        user = User()
        user.name = request.POST['name']
        user.phone = request.POST['phone']
        user.save()
        return render(request, 'create_user.html', context={'success_message': 'Success!'})


def create_car(request):
    if request.method == 'GET':
        return render(request, 'create_car.html')

    elif request.method == 'POST':
        brand = Brand()
        model = AutoModel()
        auto = Auto()
        brand.name = request.POST['brand']
        model.name = request.POST['model']
        auto.vin_code = request.POST['vin']

        d = Brand.objects.all()
        w = []
        for i in d:
            w += [i.name]

        if brand.name in w:
            brid = Brand.objects.filter(name=brand.name)
            model.brand_id = brid[0].id
            model.save()
            auto.auto_model_id = model.pk
            auto.save()
            return render(request, 'create_car.html', context={'success_message': 'Success!'})

        else:
            brand.save()
            model.brand_id = brand.pk
            model.save()
            auto.auto_model_id = model.pk
            auto.save()
            return render(request, 'create_car.html', context={'success_message': 'Success!'})


def book_or_take(request):
    if request.method == 'GET':
        return render(request, 'book_or_take.html')

    elif request.method == 'POST':
        auto_id = request.POST['idauto']
        userid = request.POST['iduser']
        autostatus = request.POST['status']
        Auto.objects.filter(id=auto_id).update(user_id=userid, status=autostatus)
        # or
        # au = Auto.objects.get(id=auto_id)
        # au.status = autostatus
        # au.user_id = userid
        # au.save(update_fields=["status"])
        # au.save(update_fields=["user_id"])

        return render(request, 'book_or_take.html', context={'success_message': 'Success!'})
