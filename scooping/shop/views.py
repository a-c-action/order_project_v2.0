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
    foods =Menu.objects.filter(ctype="简餐").all()
    paginator = Paginator(foods, 9)
    print(paginator.page_range)

    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    # print(locals())
    return render(request, 'shop.html', locals())

def server01(request):
    '''分页显示当前的菜单数据'''
    ctype=request.GET['ctype']
    # print(ctype)

    foods =Menu.objects.filter(ctype=ctype).all()
    print(foods)
    paginator = Paginator(foods, 9)
    print(paginator.page_range)

    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    jsonStr=serializers.serialize("json",page)
    return HttpResponse(jsonStr)

def server02(request):
    content=request.GET["content"]
    foods=Menu.objects.filter(cname__contains=content).all()
    print(foods)
    paginator = Paginator(foods, 9)
    print(paginator.page_range)

    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    jsonStr = serializers.serialize("json", page)
    return HttpResponse(jsonStr)

