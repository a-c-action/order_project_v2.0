from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from django.contrib import messages


# Create your views here.


def book_table(request):
    if request.method == "POST":
        time = request.POST.get("time")
        date = request.POST.get("date")
        person = request.POST.get("person")
        table = request.POST.get("table")
        phone = request.POST.get("phone")
        html="time:"+time+"date:"+date+"person:"+person+"table:"+table+"phone:"+phone


        return HttpResponse(html)




