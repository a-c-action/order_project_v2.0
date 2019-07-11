from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from django.contrib import messages
from . import models
from django.core import serializers
import json



# Create your views here


def book_table(request):
 
    value=request.session['user']["uaccount"]
    time = request.POST.get("timetable")
    data = request.POST.get("datatable")
    person = request.POST.get("personnum")
    table = request.POST.get("tablenum")
    phone = request.POST.get("phone")
    uid=models.UserProfile.objects.get(uname=value)
    order=models.Order_from.objects.create(check_data=data,check_time=time,check_person=person,
                                            check_phone=phone, check_table=table, uid=uid)
    # order.save()
    # html="time:"+time+"date:"+data+"person:"+person+"table:"+table+"phone:"+phone
    # print(html)
    tableall = ['桌号1', '桌号2', '桌号3', '桌号5', '桌号6', '桌号8', '桌号9', '桌号10']
    tables = models.Order_from.objects.filter(check_data=data, check_time=time)
    print(tables)
    if tables:
        for table in tables:
            if table.check_table in tableall:
                tableall.remove(table.check_table)
    str = json.dumps(tableall)
    return HttpResponse(str)


def checktable(request):
    tableall=['桌号1','桌号2','桌号3','桌号5','桌号6','桌号8','桌号9','桌号10']
    time=request.GET.get("timetable")
    data=request.GET.get("datatable")
    tables=models.Order_from.objects.filter(check_data=data,check_time=time)
    print(tables)
    if tables:
        for table in tables:
            if table.check_table in tableall:
                tableall.remove(table.check_table)
    str=json.dumps(tableall)
    return HttpResponse(str)






