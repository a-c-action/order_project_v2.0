from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.payment),
    # url(r'^\?orderid=(\d+)',views.pay_list),
    url(r'^glob_search',views.glob_search),
    url(r'^search_server',views.search_server),
    url(r'^do_pay',views.do_pay),
    url(r'^pay',views.payment_new),
]