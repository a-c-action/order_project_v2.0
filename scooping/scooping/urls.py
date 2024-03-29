"""scooping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$",views.index),
    url(r"^scoping/",include("scoping.urls")),
    url(r"^about/",include("about.urls")),
    url(r"^checkout/",include("checkout.urls"),),
    url(r"^userinfo/",include("userinfo.urls")),
    url(r"^payment/",include("payment.urls")),
    url(r"^shop/",include("shop.urls")),
    url(r"^single/",include("single.urls")),
    url(r"^order/",include("order.urls")),
]
