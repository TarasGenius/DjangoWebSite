from django.urls import path
from Shop.views import shop_list, shop_detail, shop_buy, shop_category, goods_create, goods_update


urlpatterns = [
    path('', shop_list),
    path('detail/<int:id>/', shop_detail),
    path('buy/', shop_buy),
    path('category/', shop_category),
    path('create/', goods_create),
    path('update/<int:id>/', goods_update),

]