from django.shortcuts import render
import json


from . import models
from single.models import Menu
from userinfo.models import UserProfile

from decimal import *

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.filter(uname=username)
    print(users)
    carts=models.Shoppingcart.objects.filter(sid=users)
    return render(request, 'checkout.html',locals())







