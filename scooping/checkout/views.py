from django.shortcuts import render
import json

from . import models
from single.models import Menu
from decimal import *

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'checkout.html')



caipinlist=[]
caipinlistinfo=[]
def new_dish_info(request):
    cname=request.GET["cname"]
    print(cname)
    dic={}
    if cname not in caipinlist:
        caipinlist.append(cname)
        caipin=Menu.objects.get(cname=cname)
        print("price",caipin.cprice,type(caipin.cprice))
        dic["cname"]=caipin.cname
        dic["cprice"]=str(caipin.cprice.quantize(Decimal('0.0')))
        dic["cmarket_price"]=str(caipin.cmarket_price.quantize(Decimal('0.0')))
        # dic["pic"]=caipin.pic
        caipinlistinfo.append(dic)
    # caipinlistinfos=json.dumps(caipinlistinfo)
    print(caipinlistinfo)
    return HttpResponse("添加成功")


def dish_info_list(request):
    print("新的列表", caipinlistinfo)
    dic = {}
    jsonStr = json.dumps(caipinlistinfo)
    dic["infoit"] = caipinlistinfo
    print("薪资点",dic)
    return HttpResponse(jsonStr)
