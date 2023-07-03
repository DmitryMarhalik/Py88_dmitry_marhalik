from django.shortcuts import render
from .forms import AutoForm
from .models import User, AutoModel, Auto, Brand

def main_page(request):
    auto = Auto.objects.all().order_by('id')
    # nm = []
    # for n in auto:
    #     if n.user_id == None:
    #         n.user_id = "-"
    #         nm += n.user_id
    #     else:
    #         p = User.objects.filter(pk=n.user_id)
    #         for i in p:
    #             nm += [i.name]
    dict = {"auto": auto} #"name": nm}
    return render(request, 'main.html', context=dict)


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
        auto_form=AutoForm
        return render(request, 'create_car.html',context={'form':auto_form})

    elif request.method == 'POST':
        error=None
        auto_form=AutoForm(request.POST)
        if auto_form.is_valid():
            auto_form.save()
        else:
            error="error form"
        # brand = Brand()
        # modl = AutoModel()
        # auto = Auto()
        # brand.name = request.POST['brand']
        # modl.name = request.POST['model']
        # auto.vin_code = request.POST['vin']
        #
        # d = Brand.objects.all()
        # w = []
        # for i in d:
        #     w += [i.name]
        #
        # if brand.name in w:
        #     brid = Brand.objects.filter(name=brand.name)
        #     modl.brand_id = brid[0].id
        #     modl.save()
        #     auto.auto_model_id = modl.pk
        #     auto.save()
        # #     return render(request, 'create_car.html', context={'success_message': 'Success!'})
        #
        # else:
        #     brand.save()
        #     modl.brand_id = brand.pk
        #     modl.brand_id = brand.pk
        #     modl.save()
        #     auto.auto_model_id = modl.pk
        #     auto.save()
            return render(request, 'create_car.html', context={'success_message': 'Success!','error':error})


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
