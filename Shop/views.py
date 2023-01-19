from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Shop.models import Goods



def shop_list(request):
    a = Goods.objects.all()
    context = {
        'title': 'Shop List',
        'object': a

    }
    return render(request, 'shop list.html', context)

def shop_detail(request, id=None):
    instance = get_object_or_404(Goods, id=id)
    context = {
        'title': 'Details',
        'object': instance

    }
    return render(request, 'shop detail.html', context)

def shop_buy(request):
    return HttpResponse('<h1>Shop_buy</h1>')

def shop_category(request):
    a = Goods.objects.all()
    context = {
        'title': 'Category',
        'object': a


    }
    return render(request, 'Shop category.html', context)


