from django.shortcuts import render
from . import models

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'checkout.html')


def new_dish_info(request):
    name=request.GET
    print("msg",name)
    return HttpResponse("添加成功")