from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$",views.food_page,name="food"),
    url(r"^food_server/",views.server01),
    url(r"^search_server/",views.server02),
]