from django.db import models


# Create your models here.

# import sys
# sys.path.append('/home/tarena/PycharmProjects/order_project_v2.0/scooping/userinfo')
# sys.path.append('/home/tarena/PycharmProjects/order_project_v2.0/scooping/single')
from userinfo.models import UserProfile
from single.models import Menu



# 订单表
class Ordertable(models.Model):
    data=models.DateField("订单日期")
    orderid=models.CharField("订单编号",max_length=30)
    table = models.CharField("桌号", max_length=30)
    allmoney=models.DecimalField("订单金额",max_digits=7,decimal_places=2)
    otype=models.IntegerField("订单状态")
    odish=models.IntegerField("配餐状态")
    #一个用户可以有多个订单
    uid = models.ForeignKey(UserProfile)
    class Meta:
        db_table='Ordertable'

#订单明细表
class Orderlist(models.Model):
    lcount=models.IntegerField("菜品数量")
    lmoney=models.DecimalField("菜品金额",max_digits=7,decimal_places=2)
    #一个订单编号可以对应多个明细
    check_id=models.ForeignKey(Ordertable)
    #一个明细对应一个菜品
    cid=models.OneToOneField(Menu)
    class Meta:
        db_table='Orderlist'