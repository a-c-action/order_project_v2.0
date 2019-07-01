from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from io import BytesIO
from . import verify_code
from django.conf import settings
import os,re
from . import models
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
# Create your views here.

def login(request):
    if request.method=='GET':
        uaccount = request.COOKIES.get('uaccount','')
        return render(request,"login.html",locals())
    elif request.method=='POST':
        remember = request.POST.get('remember','')
        uaccount = request.POST.get('uaccount','')
        password = request.POST.get('password','')
        try:
            user = models.Users_auths.objects.get(Q(uname=uaccount) | Q(uemail=uaccount) | Q(uphone=uaccount))
            request.session['user'] = {
                'uaccount': user.uname,
                'id': user.id
            }
            if check_password(password,user.password):
                resp = HttpResponse("登陆成功")
                if remember:
                    resp.set_cookie('uaccount', user.uname, 7 * 24 * 60 * 60)
                else:
                    resp.delete_cookie('username')
                return render(request,"index.html")
            else:
                return HttpResponse("登陆失败,密码不正确")
        except:
            return HttpResponse("登陆失败,没有此用户")

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        # 将网页位置重定向
        return HttpResponseRedirect("/")

def verify_code_img(request):
    buf = BytesIO()  # 直接在内存开辟一点空间存放临时生成的图片
    img, codes = verify_code.verify_code()#利用上面的模块得到img对象和验证码code
    img.save(buf, "png")  # 写入内存
    data = buf.getvalue()  # 从内存中读出
    print(data)
    with open(os.path.join(settings.UPLOAD_DIRS,"code.png"),'wb') as f:
        img.save(f,format='png')
    request.session['verify_code'] = codes
    return HttpResponse(data,'image/png')
    # return render(request,'login.html')

def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    elif request.method == "POST":
        username = request.POST.get('uname', '')
        uemail = request.POST.get('uemail', '')
        password = request.POST.get('upassword', '')
        password2 = request.POST.get('upassword2', '')
        password = make_password(password,"a",'pbkdf2_sha1')
        password2 = make_password(password2,"a",'pbkdf2_sha1')
        uphone = request.POST.get('uphone','')
        # verification_code = request.POST.get('verification_code','')
        # activation_code = request.POST.get('activation_code','')
        if username == '':
            username_error='用户名为空'
            return render(request,'register.html',locals())
        # if not re.findall('^[a-zA-Z][a-zA-Z0-9_-]{3,15}$',username):
        #     username_error = '用户名不符合要求'
        #     return render(request, 'register.html', locals())
        # if not re.findall('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$',uemail):
        #     uemail_error = '邮箱不符合要求'
        #     return render(request, 'register.html', locals())
        if password == '':
            return HttpResponse('密码不能为空')
        # if not re.findall('^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$',password):
        #     password_error = '密码强度太低'
        #     return render(request, 'register.html', locals())
        if password != password2:
            return HttpResponse('两次输入密码不一致')
        # if not re.findall('^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$',uphone):
        #     uphone_error = '手机号不正确'
        #     return render(request, 'register.html', locals())
        # if verification_code != request.session['verify_code']:
        #     return HttpResponse('验证码不正确')
        # if activation_code != request.session['activation_code']:
        #     return HttpResponse('激活码不正确')
        try:
            user = models.UserProfile.objects.create(
                uname=username,
                uphone=uphone,
                uemail=uemail,
            )
            user2 = models.Users_auths.objects.create(
                uname=username,
                uphone=uphone,
                uemail=uemail,
                password=password,
                userprofile=user,
            )
            return render(request,'login.html')
        except:
            return HttpResponse("注册失败")

def RetrievePassword(request):
    if request=="GET":
        return render(request,"RetrievePassword.html")
    elif request=="POST":
        return HttpResponse("修改")