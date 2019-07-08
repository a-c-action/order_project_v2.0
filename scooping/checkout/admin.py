from django.contrib import admin

# Register your models here.

from . import models

class MenuManager(admin.ModelAdmin):
    list_display = ['id','ctype','cname','cprice','cmarket_price','pic']
    list_display_links = ['id','ctype','cname']
    list_filter = ['id','ctype','cname']
    search_fields = ['id','ctype','cname']
admin.site.register(models.Menu,MenuManager)

class MenuInfoManager(admin.ModelAdmin):
    list_display = ['id','introduct','value','infor','cid']
    list_display_links = ['id','introduct','value','infor','cid']
    list_filter = ['id','infor']
    search_fields = ['id','infor']
admin.site.register(models.MenuInfo,MenuInfoManager)

class ShoppingcartManager(admin.ModelAdmin):
    list_display = ['id','cname','cprice','pic','number','sid']
    list_display_links = ['id','cname','cprice','pic','number','sid']
    list_filter = ['id','cname']
    search_fields = ['id','cname']
admin.site.register(models.Shoppingcart,ShoppingcartManager)

class OrdertableManager(admin.ModelAdmin):
    list_display = ['id','data','orderid','table','allmoney','otype','odish']
    list_display_links = ['id','data','orderid','table','allmoney','otype','odish']
    list_filter = ['id','orderid']
    search_fields = ['id','orderid']
admin.site.register(models.Ordertable,OrdertableManager)

class OrderlistManager(admin.ModelAdmin):
    list_display = ['id','lcount','lmoney','check_id','cid']
    list_display_links = ['id','lcount','lmoney','check_id','cid']
    list_filter = ['id']
    search_fields = ['id']
admin.site.register(models.Orderlist,OrderlistManager)\

class TakeoutManager(admin.ModelAdmin):
    list_display = ['id','name','phone','addr','number','oid']
    list_display_links = ['id','name','phone','addr','number','oid']
    list_filter = ['id']
    search_fields = ['id']
admin.site.register(models.Takeout,TakeoutManager)