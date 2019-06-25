from django.http import HttpResponse
from django.shortcuts import render

#返回主页面
def index(request):
    return render(request,"index.html")

