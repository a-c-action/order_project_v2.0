# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-11 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20190710_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertable',
            name='otype',
            field=models.IntegerField(default='1', verbose_name='订单状态'),
        ),
    ]
