from django.shortcuts import render
from django.http import HttpResponse


def shop_list(request):
    return HttpResponse('<h1>Shop_list</h1>') # dcs

def shop_detail(request):
    return HttpResponse('<h1>Shop_detail</h1>')

def shop_buy(request):
    return HttpResponse('<h1>Shop_buy</h1>')

def shop_list(request):
    return HttpResponse('<h1>Shop_list</h1>')
