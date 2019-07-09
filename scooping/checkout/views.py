from django.shortcuts import render
import json


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







