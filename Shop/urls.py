from django.urls import path
from Shop.views import shop_list, shop_detail, shop_buy, shop_category, goods_create, goods_update, goods_delete

app_name = 'shop'

urlpatterns = [
    path('', shop_list, name='shop_list'),
    path('detail/<int:id>/', shop_detail, name='shop_detail'),
    path('buy/', shop_buy, name='shop_buy'),
    path('category/', shop_category, name='shop_category'),
    path('create/', goods_create, name='goods_create'),
    path('update/<int:id>/', goods_update, name='goods_update'),

]