from django.contrib import admin
from Shop.models import Goods


class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'update', 'create')
    search_fields = ('id',)
    list_filter = ('price', 'create', 'title')


admin.site.register(Goods, GoodsModelAdmin)

