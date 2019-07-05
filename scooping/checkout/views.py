from django.shortcuts import render
from . import models

from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'checkout.html')


def new_dish_info(request, dish_id):

    try:
        adish = models.MenuInfo.objects.get(id=dish_id)
        apic = models.Menu.objects.get(id=dish_id)
        # return render(request, 'checkout.html')

    except:
        return HttpResponse("没有找到ID为 " + dish_id + "的菜品")

    if request.method == 'GET':

        info = models.Menu.objects.all()
        return render(request, 'checkout.html', locals())
        # return render(request, "single.html", locals())
    elif request.method == 'POST':
        try:
            # apic = models.Dish.objects.get(id=dish_id+4)

            cprice = request.POST.get('cprice', '0.0')
            adish.cprice = cprice
            # pict = DishInfo.cid.pic

            # m_price = request.POST.get('market_price', '0.0')
            # adish.market_price = m_price
            # adish.save()  # 提交成功
        #     return HttpResponse("修改成功")
        except:
            return HttpResponse("没有该菜品")