from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.single),
    url(r'^new/(\d+)$',views.new_dish_info),
    url(r'^new1$',views.dish_info),

]