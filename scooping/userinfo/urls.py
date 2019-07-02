from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$',views.login),
    url(r'^register$', views.register),
    url(r'^RetrievePassword$',views.RetrievePassword),
    url(r'^verify_code', views.verify_code_img),
    url(r'^logout$',views.logout)
]