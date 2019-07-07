from django.contrib import admin

# Register your models here.

from . import models

class UserProfileManager(admin.ModelAdmin):
    list_display = ['id','uname','uphone','uemail','register_time','last_login_time','integral']
    list_display_links = ['id','uname']
    list_filter = ['id','uname']
    search_fields = ['id','uname']
admin.site.register(models.UserProfile,UserProfileManager)

class Users_authsManager(admin.ModelAdmin):
    list_display = ['id','uname','uphone','uemail','password','login_status','userprofile']
    list_display_links = ['id','uname','uphone','uemail','login_status']
    list_filter = ['id','uname','login_status']
    search_fields = ['id','uname','uphone','uemail','login_status']
admin.site.register(models.Users_auths,Users_authsManager)