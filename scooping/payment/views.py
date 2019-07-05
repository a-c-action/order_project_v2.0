from django.shortcuts import render
from django.http import HttpResponse
from userinfo.models import UserProfile
from checkout import models
from django.db.models import Q
# Create your views here.


def payment(request):
    orderid = request.GET['orderid']
    if orderid:
        id = models.Ordertable.objects.get(orderid=orderid).id
        # print('订单id是：'+str(id))
        #根据订单号对应的id找到orderlist表中的记录
        results = models.Orderlist.objects.filter(check_id_id=id)

        #对应找到Menu中的菜品信息，并将其id组成字典
        menu_list_id = []
        for re in results:
            print('对应的菜品id',re.cid_id)
            menu_list_id.append(re.cid_id)
        pay = 0
        print('对应的菜品id：',menu_list_id)
        menu_list = []
        for i in menu_list_id:
            item = models.Menu.objects.get(id=i)
            menu_dic = {}
            menu_dic['pic']=item.pic
            menu_dic['name'] = item.cname
            menu_dic['cprice'] = item.cprice
            pay += int(item.cprice)
            menu_list.append(menu_dic)



        #
        print('订单列表：',menu_list)

        return render(request,'payment.html',locals())

def pay_list(request):
    return HttpResponse('接到id')