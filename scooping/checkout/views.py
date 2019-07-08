from django.shortcuts import render
import json

from . import models
from single.models import Menu
from userinfo.models import UserProfile
from decimal import *

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'checkout.html')




def new_dish_info(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.filter(uname=username)
    print(users)
    cname=request.GET["cname"]
    caipin = Menu.objects.get(cname=cname)
    cname = caipin.cname
    cprice = str(caipin.cprice.quantize(Decimal('0.0')))
    cimg = caipin.pic
    # if cname not in caipinlist:
    #         pass
    return HttpResponse("添加成功")


# def dish_info_list(request):
#     print("新的列表", caipinlistinfo)
#     dic = {}
#     jsonStr = json.dumps(caipinlistinfo)
#     dic["infoit"] = caipinlistinfo
#     print("薪资点",dic)
#     return HttpResponse(jsonStr)
