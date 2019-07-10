from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.single),
    url(r'^new/(\d+)$',views.new_dish_info),
    url(r'^newinfo',views.dish_info),

]