from django.shortcuts import render
from django.http import HttpResponse
from checkout import models

# Create your views here.

def order1(request):
    return  render(request,"order.html")

def all_order_list(request):
    # Order_from为订单模型类名
    # userid=request.session['user']["id"]
    # user=models.UserProfile.objects.get(id=userid)
    # order_list=user.ordertable_set.all()
    order_list=models.Ordertable.objects.all()
    print(order_list)
    orderdic={}
    for order in order_list:
        orderinfo=order.orderlist_set.all()
        orderdic[order]=orderinfo
    print(orderdic)
    return render(request,"order.html",locals())

def payend_list(request):
    # Pay_order为已付款订单模型类名
    order_list = models.Ordertable.objects.filter(otype=0)
    orderdic = {}
    for order in order_list:
        orderinfo= order.orderlist_set.all()
        orderdic[order] = orderinfo
    return render(request,"order.html",locals())

def nopay_list(request):
    # Pay_order未付款订单模型类名
    order_list = models.Ordertable.objects.filter(otype=1)
    orderdic = {}
    for order in order_list:
        orderinfo = order.orderlist_set.all()
        orderdic[order] = orderinfo
    return render(request, "order.html", locals())

def deleteit(request):
    oderid=request.GET.get("id")
    pass

def cancelit(request):
    pass
