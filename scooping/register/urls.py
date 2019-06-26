from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.register),
    url(r'register_input$',views.register_input),
]