import json
import random
import os, re
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from io import BytesIO
from . import verify_code
from . import models


# Create your views here.


def login(request):
    """
    跳转登录界面
    :param request:
    :return:
    """
    return render(request, 'login.html')


def checkuaccount(request):
    """
    检查登录账户
    :param request:
    :return:
    """
    uaccount = request.GET.get('uaccount', '')
    if uaccount:
        try:
            # 使用Q对象查询以及逻辑判断,实现用户名/邮箱/手机号登录
            user = models.Users_auths.objects.get(Q(uname=uaccount) | Q(uemail=uaccount) | Q(uphone=uaccount))
            if user.login_status == True:
                return HttpResponse("2")
            else:
                return HttpResponse("3")
        except:
            return HttpResponse("1")
    else:
        return HttpResponse("0")


def checkupassword(request):
    """
    检查密码
    :param request:
    :return:
    """
    uaccount = request.GET.get('uaccount', '')
    if uaccount:
        upassword = request.GET.get('upassword', '')
        if upassword:
            try:
                user = models.Users_auths.objects.get(Q(uname=uaccount) | Q(uemail=uaccount) | Q(uphone=uaccount))
                if check_password(upassword, user.password):
                    return HttpResponse("2")
                else:
                    return HttpResponse("3")
            except:
                return HttpResponse("4")
        else:
            return HttpResponse("1")
    else:
        return HttpResponse("0")


def check_verify_code(request):
    """
    检查图片验证码
    :param request:
    :return:
    """
    verify_code = request.GET.get('verify_code', '')
    if verify_code:
        if verify_code.lower() != request.session["verify_code"].lower():
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        return HttpResponse("0")


def checklogin(request):
    """
    检查登录
    :param request:
    :return:
    """
    remember = request.POST['remember']
    uaccount = request.POST['uaccount']
    password = request.POST['upassword']
    verify_code = request.POST['verify_code']
    if uaccount == '':
        return HttpResponse("用户名为空")
    else:
        try:
            user = models.Users_auths.objects.get(Q(uname=uaccount) | Q(uemail=uaccount) | Q(uphone=uaccount))
            # 将user.name & user.id存在session中
            request.session['user'] = {
                'uaccount': user.uname,
                'id': user.id
            }
            if user.login_status == True:
                return HttpResponse("登陆失败,你已登录")
            else:
                if verify_code.lower() != request.session["verify_code"].lower():
                    return HttpResponse('验证码不正确')
                else:
                    if check_password(password, user.password):
                        auser = models.Users_auths.objects.get(uname=user.uname)
                        auser.login_status = True
                        auser.save()
                        auser1 = models.UserProfile.objects.get(uname=user.uname)
                        auser1.login_time = time.strftime("%Y %m %d  %H:%M:%S", time.localtime())
                        auser1.save()
                        resp = HttpResponse("登陆成功")
                        # 判断是否勾选自动登录,将用户名存在Cookies中
                        if remember:
                            resp.set_cookie('uaccount', user.uname, 7 * 24 * 60 * 60)
                        else:
                            resp.delete_cookie('uaccount')
                        msg = "登陆成功"
                        return HttpResponse(msg)
                    else:
                        return HttpResponse("登陆失败,密码不正确")
        except:
            return HttpResponse("登陆失败,没有此用户")


def verify_code_img(request):
    """
    获取生成的验证码
    :param request:
    :return:
    """
    img, codes = verify_code.verify_code()  # 利用verify_code模块得到img对象和验证码codes
    buf = BytesIO()  # 直接在内存开辟一点空间存放临时生成的图片
    img.save(buf, "png")  # 写入内存
    data = buf.getvalue()  # 从内存中读出
    request.session['verify_code'] = codes
    return HttpResponse(data, 'image/png')


def register(request):
    """
    跳转注册界面
    :param request:
    :return:
    """
    return render(request, 'register.html')


def checkuname(request):
    """
    检查注册用户名
    :param request:
    :return:
    """
    uname = request.GET['uname']
    users = models.Users_auths.objects.filter(uname=uname).all()
    users1 = models.UserProfile.objects.filter(uname=uname).all()
    if users or users1:
        return HttpResponse("1")
    return HttpResponse("0")


def checkuemail(request):
    """
    检查注册邮箱
    :param request:
    :return:
    """
    uemail = request.GET['uemail']
    users = models.Users_auths.objects.filter(uemail=uemail).all()
    users1 = models.UserProfile.objects.filter(uemail=uemail).all()
    if users or users1:
        return HttpResponse("1")
    return HttpResponse("0")


def checkuphone(request):
    """
    检查注册手机号
    :param request:
    :return:
    """
    uphone = request.GET['uphone']
    users = models.Users_auths.objects.filter(uphone=uphone).all()
    users1 = models.UserProfile.objects.filter(uphone=uphone).all()
    if users or users1:
        return HttpResponse("1")
    return HttpResponse("0")


def checkverifycode(request):
    """
    检查图片验证码
    :param request:
    :return:
    """
    verify_code = request.GET.get('verify_code', '')
    if verify_code:
        if verify_code.lower() != request.session["verify_code"].lower():
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        return HttpResponse("0")


def smscode(request):
    """
    生成短信验证码
    :param request:
    :return:
    """
    # !/usr/bin/env python
    # coding=utf-8
    phone = request.GET.get('phone', '')
    number = random.randint(100000, 999999)

    client = AcsClient('LTAIeUCNImn4yp21', 'M3Yxqxs3wOljHPn7EimdETr9PkDwdN', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "勺品有品")
    request.add_query_param('TemplateCode', "SMS_169902735")
    request.add_query_param('TemplateParam', "{'code':%s}" % number)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

    jionStr = {
        'number': number
    }

    return HttpResponse(json.dumps(jionStr))


def reguser(request):
    """
    检查注册
    :param request:
    :return:
    """
    uname = request.POST['uname']
    uemail = request.POST['uemail']
    uphone = request.POST['uphone']
    password = request.POST['password']
    password2 = request.POST['password2']
    password = make_password(password, "a", 'pbkdf2_sha1')
    password2 = make_password(password2, "a", 'pbkdf2_sha1')
    verify_code = request.POST['verify_code']
    action_code = request.POST['action_code']
    action_code1 = request.POST['action_code1']
    if uname == '':
        username_error = '用户名为空'
        return render(request, 'register.html', locals())
    if not re.findall('^[a-zA-Z][a-zA-Z0-9_-]{3,15}$', uname):
        username_error = '用户名不符合要求'
        return render(request, 'register.html', locals())
    if not re.findall('^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$', uemail):
        uemail_error = '邮箱不符合要求'
        return render(request, 'register.html', locals())
    if password == '':
        return HttpResponse('密码不能为空')
    if not re.findall('^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$', password):
        password_error = '密码强度太低'
        return render(request, 'register.html', locals())
    if password != password2:
        return HttpResponse('两次输入密码不一致')
    if not re.findall('^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$', uphone):
        uphone_error = '手机号不正确'
        return render(request, 'register.html', locals())
    if verify_code.lower() != request.session['verify_code'].lower():
        return HttpResponse('验证码不正确')
    if action_code != action_code1:
        return HttpResponse('激活码不正确')
    try:
        user = models.UserProfile.objects.create(
            uname=uname,
            uphone=uphone,
            uemail=uemail,
        )
        user2 = models.Users_auths.objects.create(
            uname=uname,
            uphone=uphone,
            uemail=uemail,
            password=password,
            userprofile=user,
        )
        msg = "注册成功"
        return HttpResponse(msg)
    except:
        rex = "注册失败"
        return HttpResponse(rex)


def retrievePassword(request):
    """
    跳转重置密码界面
    :param request:
    :return:
    """
    return render(request, 'retrievePassword.html')


def finduname(request):
    """
    检查用户名
    :param request:
    :return:
    """
    uname = request.GET.get('uname', '')
    if uname:
        try:
            user = models.Users_auths.objects.get(uname=uname)
            return HttpResponse("2")
        except:
            return HttpResponse("1")
    else:
        return HttpResponse("0")


def finduemail(request):
    """
    检查邮箱
    :param request:
    :return:
    """
    uname = request.GET.get('uname', '')
    uemail = request.GET.get('uemail', '')
    if uname:
        if uemail:
            try:
                user1 = models.Users_auths.objects.get(uname=uname)
                user2 = models.Users_auths.objects.get(uemail=uemail)
                if user1 == user2:
                    return HttpResponse("2")
                else:
                    return HttpResponse("4")
            except:
                return HttpResponse("1")
        else:
            return HttpResponse("0")
    else:
        return HttpResponse("3")


def finduphone(request):
    """
    检查手机号
    :param request:
    :return:
    """
    uname = request.GET.get('uname', '')
    uphone = request.GET.get('uphone', '')
    if uname:
        if uphone:
            try:
                user1 = models.Users_auths.objects.get(uname=uname)
                user2 = models.Users_auths.objects.get(uphone=uphone)
                if user1 == user2:
                    return HttpResponse("2")
                else:
                    return HttpResponse("4")
            except:
                return HttpResponse("1")
        else:
            return HttpResponse("0")
    else:
        return HttpResponse("3")


def findpassword(request):
    """
    检查新密码
    :param request:
    :return:
    """
    uname = request.GET.get('uname', '')
    if uname:
        try:
            user = models.Users_auths.objects.get(uname=uname)
            password = request.GET.get('password', '')
            if password:
                if not re.findall('^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$', password):
                    return HttpResponse("1")
                elif check_password(password, user.password):
                    return HttpResponse("2")
                else:
                    return HttpResponse("4")
            else:
                return HttpResponse("0")
        except:
            return HttpResponse("3")
    else:
        return HttpResponse("5")


def smscode1(request):
    """
    检查手机验证码
    :param request:
    :return:
    """
    # !/usr/bin/env python
    # coding=utf-8
    phone = request.GET.get('phone', '')
    number = random.randint(100000, 999999)

    client = AcsClient('LTAIeUCNImn4yp21', 'M3Yxqxs3wOljHPn7EimdETr9PkDwdN', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "勺品有品")
    request.add_query_param('TemplateCode', "SMS_169903182")
    request.add_query_param('TemplateParam', "{'code':%s}" % number)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

    jionStr = {
        'number': number
    }

    return HttpResponse(json.dumps(jionStr))


def modifyPassword(request):
    """
    修改密码
    :param request:
    :return:
    """
    uname = request.POST['uname']
    uemail = request.POST['uemail']
    uphone = request.POST['uphone']
    upassword = request.POST['upassword']
    upassword = make_password(upassword)
    action_code = request.POST['action_code']
    action_code1 = request.POST['action_code1']
    if uname == '':
        return HttpResponse("用户名为空")
    else:
        try:
            user = models.Users_auths.objects.get(uname=uname)
            if uemail == '':
                return HttpResponse("邮箱为空")
            else:
                if uemail != user.uemail:
                    return HttpResponse("邮箱与用户名不匹配")
                else:
                    if uphone == '':
                        return HttpResponse("手机号为空")
                    else:
                        if uphone != user.uphone:
                            return HttpResponse("手机号与用户名不匹配")
                        else:
                            if check_password(upassword, user.password):
                                return HttpResponse("新密码不能和旧密码一样")
                            else:
                                if action_code == '':
                                    return HttpResponse("验证码为空")
                                else:
                                    if action_code != action_code1:
                                        return HttpResponse("验证码错误")
                                    else:
                                        auser = models.Users_auths.objects.get(uname=user.uname)
                                        auser.password = upassword
                                        auser.login_status = False
                                        auser.save()
                                        return HttpResponse("修改成功")
        except:
            return HttpResponse("用户名不存在")


def logout(request):
    """
    退出登录
    :param request:
    :return:
    """
    if 'user' in request.session:
        auser = models.Users_auths.objects.get(uname=request.session["user"]["uaccount"])
        auser.login_status = False
        auser.save()
        del request.session['user']
        # 将网页位置重定向
        return HttpResponseRedirect("/")
