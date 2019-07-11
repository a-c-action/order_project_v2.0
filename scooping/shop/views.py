from django.shortcuts import render
from django.http import HttpResponse
from single.models import Menu
from django.core import serializers

from checkout.models import Shoppingcart
from userinfo.models import UserProfile
from . import models
# Create your views here.
# def shop(request):
#     return render(request,"shop.html")


from django.core.paginator import Paginator
def food_page(request):
    foods =Menu.objects.filter(ctype="简餐").all()
    return render(request, 'shop.html', locals())

def server01(request):

    ctype=request.GET['ctype']
    foods =Menu.objects.filter(ctype=ctype).all()
    jsonStr=serializers.serialize("json",foods)
    return HttpResponse(jsonStr)

def server02(request):
    content=request.GET["content"]
    foods=Menu.objects.filter(cname__contains=content).all()
    jsonStr = serializers.serialize("json", foods)
    return HttpResponse(jsonStr)

def new_dish_info(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.get(uname=username)
    print(users)

    cname=request.GET['name']
    print("fndkfn",cname)
    food=Menu.objects.get(cname=cname)
    carts=Shoppingcart.objects.filter(sid=users)
    cnamelist=[]
    for cart in carts:
        cnamelist.append(cart.cname)
    if cname in cnamelist:
        cart = Shoppingcart.objects.get(sid=users,cname=cname)
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

    return HttpResponse("添加成功")
