from django.db import models

# import sys
# sys.path.append('/home/tarena/PycharmProjects/order_project_v2.0/scooping/userinfo')

from userinfo.models import UserProfile

# Create your models here.
#订餐表
class Order_from(models.Model):
    check_data=models.DateField("订餐日期")
    check_time=models.CharField("订单时段",max_length=100)
    check_person=models.CharField("人数",max_length=50)
    check_phone=models.CharField("电话号码",max_length=50)
    check_table=models.CharField("桌号",max_length=50)
    # 一个用户可以预定多次
    uid=models.ForeignKey(UserProfile)
    class Meta:
        db_table='UOrder_from'
        verbose_name_plural = '订餐表'




