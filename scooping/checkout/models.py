from django.db import models

# Create your models here.

# import sys
# sys.path.append('/home/tarena/PycharmProjects/order_project_v2.0/scooping/userinfo')
# sys.path.append('/home/tarena/PycharmProjects/order_project_v2.0/scooping/single')
from userinfo.models import UserProfile

# 订单表
from single.models import Menu


class Ordertable(models.Model):
    data=models.DateField("订单日期",auto_now_add=True)
    orderid=models.CharField("订单编号",max_length=30)
    table = models.CharField("桌号", max_length=30)
    allmoney=models.DecimalField("订单金额",max_digits=7,decimal_places=2)
    otype=models.IntegerField("订单状态",default="1")
    odish=models.IntegerField("配餐状态",default="0")
    #一个用户可以有多个订单
    uid = models.ForeignKey(UserProfile)
    class Meta:
        db_table='Ordertable'
        verbose_name_plural = '订单表'

    def __str__(self):
        return f"id:{self.id},data:{self.data},orderid:{self.orderid},table:{self.table},allmoney:{self.allmoney},otype:{self.otype},odish:{self.odish}"

#订单明细表
class Orderlist(models.Model):
    lcount=models.IntegerField("菜品数量")
    lmoney=models.DecimalField("菜品金额",max_digits=7,decimal_places=2)
    #一个订单编号可以对应多个明细
    check_id=models.ForeignKey(Ordertable,on_delete=models.CASCADE)
    #一个明细对应一个菜品
    cid=models.ForeignKey(Menu)
    class Meta:
        db_table='Orderlist'
        verbose_name_plural = '订单明细表'
    def __str__(self):
        return f"id:{self.id},lcount:{self.lcount},lmoney:{self.lmoney}"

#外卖表
class Takeout(models.Model):
    name=models.CharField("姓名",max_length=50)
    phone=models.CharField("手机号",max_length=50)
    addr=models.CharField("地址 ",max_length=500)
    number=models.CharField("门牌号",max_length=20)
    oid = models.OneToOneField(Ordertable)
    class Meta:
        db_table='Takeout'
        verbose_name_plural = '外卖表'
    def __str__(self):
        return f"id:{self.id},name:{self.name},phone:{self.phone},addr:{self.addr},number:{self.number}"


class Shoppingcart(models.Model):
    """
    购物车明细表
    """
    cname = models.CharField(verbose_name='菜名',
                             max_length=50, default='')
    cprice = models.DecimalField('价格', max_digits=7,
                                 decimal_places=2, default=0)
    pic = models.ImageField("图片", upload_to='dishes/')
    number = models.CharField(verbose_name='数量',max_length=50,default='1')
    # 一个用户可以有多条购物车记录
    sid = models.ForeignKey(UserProfile)
    class Meta:
        db_table = 'Shoppingcart'
        verbose_name_plural = '购物车明细表'
    def __str__(self):
        return f"id:{self.id},cname:{self.cname},cprice:{self.cprice},pic:{self.pic},number:{self.number}"


