from django.shortcuts import render
from django.http import HttpResponse
from single.models import Menu
from django.core import serializers

from . import models
# Create your views here.
# def shop(request):
#     return render(request,"shop.html")


from django.core.paginator import Paginator
def food_page(request):
    '''分页显示当前的菜单数据'''
    foods =Menu.objects.all()
    paginator = Paginator(foods, 9)
    print(paginator.page_range)

    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'shop.html', locals())

def query(request):
    name = request.GET['name']
    foods=Menu.objects.filter(cname=name).all()
    msg=""
    for food in foods:
        msg += "%s_%s_%s_%s_%s_%s|" % (food.id, food.ctype,
                                       food.cname,food.cprice,food.cmarket_price,food.pic)
    msg = msg[0:-1]
    return HttpResponse(msg)