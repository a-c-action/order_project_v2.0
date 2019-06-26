from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.login),
    url(r'^verify_code',views.verify_code_img),
]