from django.db import models

# Create your models here.

#订单表
class Order_table(models.Model):
    check_data=models.DateField("订单日期")
    check_id=models.CharField("订单编号",max_length=30)
    check_table = models.CharField("桌号", max_length=30)
    check_money=models.DecimalField("订单金额",max_digits=7,decimal_places=2)
    check_type=models.IntegerField("订单状态")
    check_dish=models.IntegerField("配餐状态")
    #一个用户可以有多个订单
    uid = models.ForeignKey("用户id", User)

#订单明细表
class Order_list(models.Model):
    order_info_count=models.IntegerField("菜品数量")
    order_info_money=models.DecimalField("菜品金额",max_digits=7,decimal_places=2)
    #一个订单编号可以对应多个明细
    check_id=models.ForeignKey("订单编号",Order_table)
    #一个明细对应一个菜品
    cid=models.OneToOneField("菜品id",Menu)