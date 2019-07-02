# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-01 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uemail',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='uphone',
            field=models.CharField(max_length=30, unique=True, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='users_auths',
            name='password',
            field=models.CharField(max_length=150, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='users_auths',
            name='uemail',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='users_auths',
            name='uphone',
            field=models.CharField(max_length=30, unique=True, verbose_name='手机号'),
        ),
    ]
