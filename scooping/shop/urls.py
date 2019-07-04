from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$",views.food_page,name="food"),
    url(r"^query/",views.query),

]