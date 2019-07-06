from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.payment),
    # url(r'^\?orderid=(\d+)',views.pay_list),
]