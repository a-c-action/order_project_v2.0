from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$",views.order1),
    url(r"^all",views.all_order_list),
    url(r"^payend",views.payend_list),
    url(r"^nopay",views.nopay_list),
    url(r"^delete",views.deleteit),
    url(r"^cancel",views.cancelit),
]