from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Shop.models import Goods
from Shop.forms import GoodsForm
from django.contrib import messages



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
    instance = Goods.objects.all()
    obj = Goods()
    topic_instance = obj.get_list_topic()
    context = {
        'title': 'Category',
        'object': instance,
        'topic_list': topic_instance
    }
    return render(request, 'Shop category.html', context)

def goods_create(request):
    form = GoodsForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Item saved')
        return HttpResponseRedirect(instance.get_absolut_url())
    context = {
        'title': 'Goods Create',
        'form': form


    }
    return render(request, 'shop create.html', context)

def goods_update(request, id=None):
    instance = get_object_or_404(Goods, id=id)
    form = GoodsForm(request.POST or None,
                     instance=instance)
    if form.is_valid() and 'Create' in request.POST:
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Item saved')
        return HttpResponseRedirect(instance.get_absolut_url())
    elif 'Delete' in request.POST:
        instance.delete()
        return redirect('shop:shop_list')
    context = {
        'title': 'Goods update',
        'form': form


    }
    return render(request, 'shop create.html', context)
