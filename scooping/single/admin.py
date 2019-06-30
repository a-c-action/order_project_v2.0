from django.contrib import admin
from . import models
# Register your models here.
class Menu_set(admin.ModelAdmin):
    list_display=['ctype','cname','cprice','cmarket_price','pic']

class MenuInfo_set(admin.ModelAdmin):
    list_display=['introduct','value','infor','cid']


admin.site.register(models.Menu,Menu_set)
admin.site.register(models.MenuInfo,MenuInfo_set)