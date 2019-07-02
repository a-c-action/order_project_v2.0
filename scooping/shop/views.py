from django.shortcuts import render
from django.http import HttpResponse
from single.models import Menu

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

def category(request):
    data=request.GET["ctype"]
    foodf=Menu.objects.filter(ctype=data).all()
    return render(request,'shop.html',locals())