from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from userinfo.models import UserProfile
from checkout import models
import copy
# from single.models import *
from django.db.models import Q
# Create your views here.

menu_list2 = []
orderid2 = ''
pay2 = 0
def payment(request):
    def pays(request):
        orderid1 = request.GET.get('orderid')
        if orderid1:
            id = models.Ordertable.objects.get(orderid=orderid1).id
            # print('订单id是：'+str(id))
            #根据订单号对应的id找到orderlist表中的记录
            results = models.Orderlist.objects.filter(check_id_id=id)

            #对应找到Menu中的菜品信息，并将其id组成列表
            menu_list_id = []
            for re in results:
                print('对应的菜品id',re.cid_id)
                menu_list_id.append(re.cid_id)
            pay1 = 0
            print('对应的菜品id：',menu_list_id)
            menu_list1 = []
            for i in menu_list_id:
                item = models.Menu.objects.get(id=i)
                menu_dic = {}
                menu_dic['pic']=item.pic
                menu_dic['name'] = item.cname
                menu_dic['cprice'] = item.cprice
                pay1 += int(item.cprice)
                menu_list1.append(menu_dic)
            global menu_list2
            menu_list2=copy.deepcopy(menu_list1)
            print('订单列表：',menu_list2)
            global orderid2
            orderid2 = copy.deepcopy(orderid1)
            global pay2
            pay2 = copy.deepcopy(pay1)
        return HttpResponse("OK")
    menu_list = menu_list2
    orderid = orderid2
    pay = pay2
    pays(request)
    return render(request, 'payment.html', locals())

def glob_search(request):
    search_info = request.POST['Search']
    try :
        id = models.Menu.objects.get(cname__contains=search_info).id
        print('根据您输入的菜名找的的菜品id是：',id)
        # return HttpResponse('找到了')
        return HttpResponseRedirect('/single/new/%d'%id)
    except:
        return render(request,'not_find.html',locals())

#提供搜索过程中的提示功能
def search_server(request):
    cname = request.GET['isFind']
    if cname:
        try :
            id = models.Menu.objects.get(cname__contains=cname).id
            print('根据您输入的菜名找的的菜品id是：',id)
            return HttpResponse('温馨提示：可查询此菜品')
        except:
            return HttpResponse('温馨提示：本店可能未上线您输入的菜品......')
    else:
        return HttpResponse('温馨提示：请输入您要查询的菜品......')

#当用户支付完成后,订单列表中的订单状态发生改变
def do_pay(request):
    orderid = request.GET['orderid']
    if orderid:
        try:
            aorder = models.Ordertable.objects.get(orderid=orderid)
            print('现在的消费状态是：',aorder.otype)
            aorder.otype = 1
            aorder.save()
            pay_state = '亲，您已经支付完成，欢迎再次就餐......'
            return render(request,'do_pay.html',locals())
        except:
            pay_state = '亲，支付失败，请您仔细核对订单后再操作......'
            return render(request,'do_pay.html',locals())
