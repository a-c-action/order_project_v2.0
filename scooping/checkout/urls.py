from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^new',views.new_dish_info),
    url(r'^list',views.dish_info_list),
]