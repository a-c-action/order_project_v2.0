from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^checkuaccount$', views.checkuaccount),
    url(r'^checkupassword$', views.checkupassword),
    url(r'^check_verify_code$', views.check_verify_code),
    url(r'^checklogin$', views.checklogin),
    url(r'^register$', views.register),
    url(r'^checkuname$', views.checkuname),
    url(r'^checkuemail$', views.checkuemail),
    url(r'^checkuphone$', views.checkuphone),
    url(r'^checkverifycode$', views.checkverifycode),
    url(r'^smscode$', views.smscode),
    url(r'^reguser$', views.reguser),
    url(r'^verify_code', views.verify_code_img),
    url(r'^finduname$', views.finduname),
    url(r'^finduemail$', views.finduemail),
    url(r'^finduphone$', views.finduphone),
    url(r'^findpassword$', views.findpassword),
    url(r'^smscode1$', views.smscode1),
    url(r'^retrievePassword$', views.retrievePassword),
    url(r'^modifyPassword$', views.modifyPassword),
    url(r'^logout$', views.logout),
]
