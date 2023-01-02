from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1>Home_page</h1>')


def post_list(request):
    return HttpResponse('<h1>post_list</h1>')


def post_create(request):
    return HttpResponse('<h1>post_create</h1>')


def post_detail(request):
    return HttpResponse('<h1>post_detail</h1>')


def post_update(request):
    return HttpResponse('<h1>post_update</h1>')


def post_delete(request):
    return HttpResponse('<h1>post_delete</h1>')