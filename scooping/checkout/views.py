from django.shortcuts import render
from . import models

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'checkout.html')


def new_dish_info(request):
    id=request.GET("cname")
    print("cname",id)
    return HttpResponse("添加成功")

