
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^booktable",views.book_table),
    url(r"^checktable",views.checktable)
]