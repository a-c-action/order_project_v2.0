from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from django.contrib import messages
from . import models
from django.core import serializers
import json


# Create your views here


def book_table(request):
    if request.method=="GET":
        return render(request,"index.html")
    elif request.method == "POST":
        value=request.session['user']["uaccount"]
        time = request.POST.get("time")
        date = request.POST.get("date")
        person = request.POST.get("person")
        table = request.POST.get("table")
        phone = request.POST.get("phone")
        uid=models.UserProfile.objects.get(uname=value)
        order=models.Order_from.objects.create(check_data=date,check_time=time,check_person=person,
                                                check_phone=phone, check_table=table, uid=uid)
        # order.save()
        # html="time:"+time+"date:"+date+"person:"+person+"table:"+table+"phone:"+phone
        # print(html)
        return render(request,"index.html")


def checktable(request):
    tableall=['桌号1','桌号2','桌号3','桌号5','桌号6','桌号8','桌号9','桌号10']
    time=request.GET.get("timetable")
    data=request.GET.get("datatable")
    tables=models.Order_from.objects.filter(check_data=data,check_time=time)
    print(tables)
    for table in tables:
        tableall.remove(table.check_table)
    str=json.dumps(tableall)
    return HttpResponse(str)






