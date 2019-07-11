from django.shortcuts import render

from . import models

from django.http import HttpResponse

from .models import Menu

from userinfo.models import UserProfile
from checkout.models import  Shoppingcart
import os
# Create your views here.

def single(request):
    # return render(request,"single.html")
    # pic_obj = models.Dish.objects.get(id=1)
    # return render(request,'single.html',{'pic_obj':pic_obj})
    pic_obj = models.MenuInfo.objects.filter(id__lt=9)
    info = models.Menu.objects.filter(id__lt=9)
    return render(request, 'single.html', locals())

def new_dish_info(request, dish_id):

    try:
        adish = models.MenuInfo.objects.get(id=dish_id)
        apic = models.Menu.objects.get(id=dish_id)

    except:
        return HttpResponse('该菜品已下架，请选择其他菜品')

    if request.method == 'GET':

        info = models.Menu.objects.filter(id__lt=9)
        return render(request, 'single.html', locals())
        # return render(request, "single.html", locals())
    elif request.method == 'POST':
        try:
            # apic = models.Dish.objects.get(id=dish_id+4)

            cprice = request.POST.get('cprice', '0.0')
            adish.cprice = cprice
            # pict = DishInfo.cid.pic

            # m_price = request.POST.get('market_price', '0.0')
            # adish.market_price = m_price
            # adish.save()  # 提交成功
        #     return HttpResponse("修改成功")
        except:
            return HttpResponse("没有该菜品")


def new_dish_info01(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.get(uname=username)
    print(users)

    cname=request.GET['name']
    print("fndkfn",cname)
    food=Menu.objects.get(cname=cname)

    carts=Shoppingcart.objects.filter(sid=users)
    cnamelist = []
    for cart in carts:
        cnamelist.append(cart.cname)
    if cname in cnamelist:
        cart = Shoppingcart.objects.get(sid=users, cname=cname)
        cart.number = str(int(cart.number) + 1)
        cart.save()
    else:

        cart=Shoppingcart.objects.create(

            cname=food.cname,
            cprice=food.cprice,
            pic=food.pic,
            number="1",
            sid=users,
        )
        cart.save()

    return HttpResponse("添加成功")

def new_dish_info02(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.get(uname=username)
    print(users)

    cname = request.GET['name']
    print("fndkfn", cname)
    food = Menu.objects.get(cname=cname)

    carts = Shoppingcart.objects.filter(sid=users)
    cnamelist = []
    for cart in carts:
        cnamelist.append(cart.cname)
    if cname in cnamelist:
        cart = Shoppingcart.objects.get(sid=users, cname=cname)
        cart.number = str(int(cart.number) + 1)
        cart.save()
    else:

        cart = Shoppingcart.objects.create(

            cname=food.cname,
            cprice=food.cprice,
            pic=food.pic,
            number="1",
            sid=users,
        )
        cart.save()

    return HttpResponse("添加成功")
# def new_dish(request):
#     if request.method == "GET":
#         return render(request, 'new_dish.html')
#     elif request.method == "POST":
#
#         f1 = request.FILES['picture']
#         p = Menu()
#         p.pic = "dish/" + f1.name
#         p.save()
#         fname = settings.MEDIA_ROOT + "/dishes/" + f1.name
#         with open(fname, 'wb') as pic:
#             for i in f1.chunks():
#                 pic.write(i)
        # myfile = request.FILES['myfile']
        # print("file=",myfile)
        # print("您刚才上传的文件名称为：",myfile.name)
        # with open(os.path.join(settings.MEDIA_ROOT,myfile.name),'wb') as f:
        #     b = myfile.file.read()
        #     f.write(b)

        # return HttpResponse('添加成功')

# def dish_infor(request):
#     if request.method == "GET":
#         return render(request, 'dish_info.html')
#     elif request.method == "POST":
#         name = request.POST.get('name', '')
#         introduct = request.POST.get('introduct', '')
#         value = request.POST.get('value', '')
#         infor = request.POST.get('infor', '')
#         price = request.POST.get('price', '0')
#         market_price = request.POST.get('market_price', '0')
#         adish = models.MenuInfo.objects.create(
#             name=name,
#             introduct=introduct,
#             value=value,
#             infor=infor,
#             price=price,
#             market_price=market_price,
#         )
#         adish.save()
#         return HttpResponse('添加成功')



# def show_pic(request):
#     img = models.Dish.objects.get('image')
#     return render(request,'single.html',{'img':img})

# def show_pic(request):
#     pic_obj = models.Dish.objects.get(id=1)
#     return render(request,'single.html',{'pic_obj':pic_obj})
# # def showImg(request):
#     imgs = models.Dish.objects.all()
#     # context = {'img': imgs}
#     return render(request,'single.html',locals())
