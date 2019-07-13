from django.db import models


# Create your models here.

class UserProfile(models.Model):
    uname = models.CharField(verbose_name='用户名', max_length=30, unique=True)
    uphone = models.CharField(verbose_name='手机号', max_length=30, unique=True)
    uemail = models.EmailField(verbose_name='邮箱', unique=True)
    register_time = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    last_login_time = models.DateTimeField(verbose_name='上次登录时间', auto_now=True, null=True)
    integral = models.IntegerField(verbose_name='积分', null=True)

    class Meta:
        db_table = 'UserProfile'
        verbose_name_plural = "用户基础信息表"

    def __str__(self):
        return f"id:{self.id},用户名:{self.uname},手机号:{self.uphone},邮箱:{self.uemail},注册时间:{self.register_time},上次登录时间:{self.last_login_time},积分:{self.integral}"


class Users_auths(models.Model):
    uname = models.CharField(verbose_name='用户名', max_length=30, unique=True)
    uphone = models.CharField(verbose_name='手机号', max_length=30, unique=True)
    uemail = models.EmailField(verbose_name='邮箱', unique=True)
    password = models.CharField(verbose_name='密码', max_length=150)
    login_status = models.BooleanField(verbose_name='登录状态', default=0)
    userprofile = models.OneToOneField(UserProfile)

    class Meta:
        db_table = 'Users_auths'
        verbose_name_plural = "用户身份验证表"

    def __str__(self):
        return f"id:{self.id},用户名:{self.uname},手机号:{self.uphone},邮箱:{self.uemail},密码:{self.password},登录状态：{self.login_status}"
