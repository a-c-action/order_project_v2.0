from django.http import HttpResponse,HttpResponseRedirect

from django.utils.deprecation import MiddlewareMixin

import re

class MyMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print("中间件MyMiddleWare.process_request,方法被调用")
        if (re.match(r'^/checkout',request.path_info) or re.match(r'^/oreder',request.path_info) or re.match(r'^/payment',request.path_info)) and ('user' not in request.session):
            return HttpResponseRedirect('/userinfo/login')
        return None