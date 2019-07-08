from django.contrib import admin
from . import models
# Register your models here.
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


