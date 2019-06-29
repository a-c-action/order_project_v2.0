from django.shortcuts import render
from django.http import HttpResponse
from order import models

# Create your views here.

def order(request):
    return  render(request,"order.html")

def all_order_list(request):
    # Order_from为订单模型类名
    order_list=models.Order_list.objects.all()
    print(order_list)
    return render(request,"order.html",locals())

def payend_list(request):
    # Pay_order为已付款订单模型类名
    order = models.Order_table.objects.filter(check_type=0)
    order_list = models.Order_list.objects.filter(check_id=order)
    return render(request,"order.html",locals())

def nopay_list(request):
    # Pay_order未付款订单模型类名
    order=models.Order_table.objects.filter(check_type=1)
    order_list = models.Order_list.objects.filter(check_id=order)
    return render(request,"order.html",locals())
