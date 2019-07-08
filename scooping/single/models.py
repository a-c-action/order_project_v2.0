from django.db import models

# Create your models here.
class Menu(models.Model):
    """
    菜品表
    """
    ctype = models.CharField(verbose_name='类型',
                            max_length=50, default='')
    cname = models.CharField(verbose_name='菜名',
                            max_length=50, default='')
    cprice = models.DecimalField('价格', max_digits=7,
                                decimal_places=2, default=0)
    cmarket_price = models.DecimalField('会员价', max_digits=7,
                                       decimal_places=2,
                                       default=0)
    pic = models.ImageField("图片",upload_to='dishes/')
    class Meta:
        db_table='Menu'
        verbose_name_plural = '菜品表'
    def __str__(self):
        return  f"id:{self.id},ctype:{self.ctype},cname:{self.cname},cprice:{self.cprice},cmarket_price:{self.cmarket_price},pic:{self.pic}"

class MenuInfo(models.Model):
    """
    菜品明细表
    """
    introduct = models.CharField('菜品简介', max_length=5000, default='')
    value = models.CharField('营养价值', max_length=5000, default='')
    infor = models.CharField('产地信息', max_length=5000, default='')
    cid = models.OneToOneField(Menu)
    class Meta:
        db_table='MenuInfo'
        verbose_name_plural = '菜品明细表'
    def __str__(self):
        return f"id:{self.id},introduct:{self.introduct},value:{self.value},infor:{self.infor}"
