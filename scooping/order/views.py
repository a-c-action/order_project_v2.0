from django.shortcuts import render
from django.http import HttpResponse
from userinfo.models import UserProfile
from checkout import models
from django.db.models import Q


# Create your views here.

def order1(request):
    return  render(request,"order.html")

def all_order_list(request):
    # Order_from为订单模型类名
    username=request.session["user"]["uaccount"]
    users=UserProfile.objects.filter(uname=username)
    print(users)

    # order_list=user.ordertable_set.all()
    order_list=models.Ordertable.objects.filter(uid=users)
    print(order_list)
    orderdic={}
    for order in order_list:
        orderinfo=order.orderlist_set.all()
        orderdic[order]=orderinfo
    print(orderdic)
    return render(request,"order.html",locals())

def payend_list(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.filter(uname=username)
    print(users)
    # Pay_order为已付款订单模型类名
    order_list = models.Ordertable.objects.filter(Q(otype=0)&Q(uid=users))
    orderdic = {}
    for order in order_list:
        orderinfo= order.orderlist_set.all()
        orderdic[order] = orderinfo
    return render(request,"order.html",locals())

def nopay_list(request):
    username = request.session["user"]["uaccount"]
    users = UserProfile.objects.filter(uname=username)
    print(users)
    # Pay_order未付款订单模型类名
    order_list = models.Ordertable.objects.filter(Q(otype=1)&Q(uid=users))
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
