from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class UserProfile(AbstractUser):
#     uname = models.CharField(verbose_name='用户名',max_length=16,null=False,unique=True)
#     uphone = models.IntegerField(verbose_name='手机号',null=False)
#     uemail = models.EmailField(verbose_name='邮箱',null=False)
#     register_time = models.DateTimeField(verbose_name='注册时间',auto_now_add=True)
#     last_login_time = models.DateTimeField(verbose_name='上次登录时间',auto_now=True)
#     integral = models.IntegerField(verbose_name='积分',null=True)
#     class Meta:
#         verbose_name_plural = "用户基础信息表"
#     def __str__(self):
#         return f"id:{self.id},姓名:{self.uname},手机号:{self.uphone},邮箱:{self.uemail},注册时间:{self.register_time},上次登录时间:{self.last_login_time},积分:{self.integral}"
#
# class Users_auths(AbstractUser):
#     identity_type = models.CharField(verbose_name='身份类型',max_length=10)
#     identifier = models.CharField(verbose_name='标识符',max_length=30)
#     credential = models.CharField(verbose_name='密码凭证',max_length=16)
#     userprofile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
#     class Meta:
#         verbose_name_plural = "用户身份验证表"
#     def __str__(self):
#         return f"id:{self.id},身份类型:{self.identity_type},标识符:{self.identifier},密码凭证:{self.password}"