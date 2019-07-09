from django.shortcuts import render
import json


from . import models
from single.models import Menu
from userinfo.models import UserProfile
from django.db.models import Count
from decimal import *

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def homepage(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.filter(uname=username)
    print(users)
    carts=models.Shoppingcart.objects.filter(sid=users)
    princes={}

    for cart in carts:
        number=int(cart.number)
        price=cart.cprice*number
        princes[cart.cname]=price
        print(price)
    return render(request, 'checkout.html',locals())

def addcart(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.filter(uname=username)
    cname=request.GET["cname"]
    print("cname",cname)
    cart=models.Shoppingcart.objects.get(cname=cname,sid=users)
    cart.number=str(int(cart.number)+1)
    cart.save()
    print("number",cart.number,type(cart.number))
    return HttpResponse("OK")

def minus(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.filter(uname=username)
    cname=request.GET["cname"]
    print("cname",cname)
    cart=models.Shoppingcart.objects.get(cname=cname,sid=users)
    if int(cart.number)>1:
        cart.number=str(int(cart.number)-1)
        cart.save()
    # print("number",cart.number,type(cart.number))
    else:
        cart.number = str(int(cart.number))
        cart.save()
    return HttpResponse("OK")

def del_cuisine(request, cuisine_id):
    try:
        agreens = models.Shoppingcart.objects.get(id=cuisine_id)
        agreens.delete()
        return HttpResponseRedirect('/checkout')
    except:
        return HttpResponse("没有找到ID为" + cuisine_id + "的菜品信息,删除失败")






