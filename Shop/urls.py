from django.urls import path
from Shop.views import shop_list, shop_detail, shop_buy, shop_category


urlpatterns = [
    path('', shop_list),
    path('detail/<int:id>/', shop_detail),  #  Більше неможу придумати вюшок для магазину крім
    path('buy/', shop_buy),        #  основного листа, детальної інформації про окремий товар та
    path('category/', shop_category),                               #  сторінки покупки товару(де залишаютьть адресу і номер для зворотнього звязку)
]