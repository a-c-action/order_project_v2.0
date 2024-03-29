# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-08 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30, unique=True, verbose_name='用户名')),
                ('uphone', models.CharField(max_length=30, unique=True, verbose_name='手机号')),
                ('uemail', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('last_login_time', models.DateTimeField(auto_now=True, null=True, verbose_name='上次登录时间')),
                ('integral', models.IntegerField(null=True, verbose_name='积分')),
            ],
            options={
                'verbose_name_plural': '用户基础信息表',
                'db_table': 'UserProfile',
            },
        ),
        migrations.CreateModel(
            name='Users_auths',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30, unique=True, verbose_name='用户名')),
                ('uphone', models.CharField(max_length=30, unique=True, verbose_name='手机号')),
                ('uemail', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=150, verbose_name='密码')),
                ('login_status', models.BooleanField(default=0, verbose_name='登录状态')),
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserProfile')),
            ],
            options={
                'verbose_name_plural': '用户身份验证表',
                'db_table': 'Users_auths',
            },
        ),
    ]
