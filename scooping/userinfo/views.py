from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
# import random
# from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from . import verify_code
from django.conf import settings
import os

# Create your views here.
# from scooping.register import models


# class CustomBackend(ModelBackend):
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user = models.UserProfile.objects.get(Q(uname=username) | Q(uemail=username) | Q(uphone=username))
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None

def login(request):
    if request.method=='GET':
        uname = request.COOKIES.get('uname','')
        return render(request,"login.html",locals())
    elif request.method=='POST':
        remember = request.POST.get('remember','')
        uname = request.POST.get('uname','')
        credential = request.POST.get('credential','')
        # try:

def verify_code_img(request):
    buf = BytesIO()  # 直接在内存开辟一点空间存放临时生成的图片
    img, codes = verify_code.verify_code()#利用上面的模块得到img对象和验证码code
    img.save(buf, "png")  # 写入内存
    data = buf.getvalue()  # 从内存中读出
    print(data)
    with open(os.path.join(settings.UPLOAD_DIRS,"code.png"),'wb') as f:
        img.save(f,format='png')
    # 将验证码存在各自的session中，这样做的好处是每个人都有自己的验证码，不会相互混淆（一定不能设为全局变量）
    request.session['verify_code'] = codes
    # return HttpResponse(data,'image/png')
    return render(request,'login.html')

def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    elif request.method == "POST":
        pass


def RetrievePassword(request):
    return render(request,"RetrievePassword.html")
