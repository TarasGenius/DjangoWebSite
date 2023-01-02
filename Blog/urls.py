from django.urls import path
from Blog.views import post_list, post_create, post_delete, post_detail, post_update

urlpatterns = [
    path('', post_list),
    path('create/', post_create),
    path('delete/', post_delete),
    path('detail', post_detail),
    path('update', post_update),

]