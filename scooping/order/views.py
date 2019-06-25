from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def order(request):
    return  render(request,"order.html")

def all_order_list(request):
    # Order_from为订单模型类名
    order_list=models.Order_from.objects.all()
    return render(request,"order.html",locals())

def payend_list(request):
    # Pay_order为已付款订单模型类名
    order_list=models.Pay_order.objects.filter()
    return render(request,"order.html",locals())

def nopay_list(request):
    # Pay_order未付款订单模型类名
    order_list=models.Order_completed.objects.filter()
    return render(request,"order.html",locals())