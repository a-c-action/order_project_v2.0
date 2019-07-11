import json
import time
from django.shortcuts import render
from django.db.models import Q
from . import models
from single.models import Menu
from userinfo.models import UserProfile
from django.db.models import Count
from decimal import *
from django.http import HttpResponse

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

def generate_orders(request):
    username = request.session["user"]["uaccount"]
    user = UserProfile.objects.get(uname = username)
    cart_table = request.POST['cart_table']
    number = request.POST['number']
    order_number = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-2:]
    print(order_number)
    allmoney = 0
    for i in range(0,int(number)-1):
        cname = request.POST['cname%s'%i]
        order = models.Shoppingcart.objects.get(Q(sid=user)&Q(cname=cname))
        allmoney += order.cprice*int(order.number)
    cart_order_table = models.Ordertable.objects.create(
        orderid = order_number,
        table = cart_table,
        allmoney = allmoney,
        uid = user,
    )
    shopping_cart = models.Ordertable.objects.get(orderid=order_number)
    for i in range(0,int(number)-1):
        cname = request.POST['cname%s'%i]
        order = models.Shoppingcart.objects.get(Q(sid=user) & Q(cname=cname))
        menu = models.Menu.objects.get(cname=cname)
        cart_order_list = models.Orderlist.objects.create(
            lcount = order.number,
            lmoney = order.cprice*int(order.number),
            check_id = shopping_cart,
            cid = menu,
        )
    whether = request.POST['whether']
    if whether == "是":
        takename = request.POST['takename']
        takephone = request.POST['takephone']
        takeaddress = request.POST['takeaddress']
        takenumber = request.POST['takenumber']
        print(takename)
        print(takephone)
        print(takeaddress)
        print(takenumber)
        takeout = models.Takeout.objects.create(
            name = takename,
            phone = takephone,
            addr = takeaddress,
            number = takenumber,
            oid = shopping_cart,
        )
    print(order_number)
    return HttpResponse(order_number)

