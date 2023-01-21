from django.urls import path
from Shop.views import shop_list, shop_detail, shop_buy, shop_category, goods_create


urlpatterns = [
    path('', shop_list),
    path('detail/<int:id>/', shop_detail),
    path('buy/', shop_buy),
    path('category/', shop_category),
    path('create/', goods_create),
]