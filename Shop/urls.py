from django.urls import path
from Shop.views import shop_list, shop_detail, shop_buy


urlpatterns = [
    path('', shop_list),
    path('detail/', shop_detail),  #  Більше неможу придумати вюшок для магазину крім
    path('buy/', shop_buy),        #  основного листа, детальної інформації про окремий товар та
                                   #  сторінки покупки товару(де залишаютьть адресу і номер для зворотнього звязку)
]