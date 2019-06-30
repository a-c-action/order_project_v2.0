from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from django.contrib import messages
from . import models


# Create your views here


def book_table(request):
    if request.method=="GET":
        return render(request,"index.html")
    if request.method == "POST":
        value=request.COOKIES.get('user')
        time = request.POST.get("time")
        date = request.POST.get("date")
        person = request.POST.get("person")
        table = request.POST.get("table")
        phone = request.POST.get("phone")
        uid=models.UserProfile.objects.get(uname=value)
        order=models.Order_from.objects.create(check_data=date,check_time=time,check_person=person,
                                                check_phone=phone, check_table=table, uid=uid)
        order.save()
        html="time:"+time+"date:"+date+"person:"+person+"table:"+table+"phone:"+phone


        return HttpResponse(html)




