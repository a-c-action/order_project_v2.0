from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^generate$',views.generate_orders),
    url(r'^add', views.addcart),
    url(r'^minus', views.minus),
    url(r'^del/(\d+)$', views.del_cuisine)
]