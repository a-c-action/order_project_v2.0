from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^food$",views.food_page,name="food"),
    url(r"^category$",views.category),
]