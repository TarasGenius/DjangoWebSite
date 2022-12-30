from django.contrib import admin
from Blog.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'update')
    list_filter = ('price',)
    list_display_links = ('title',)
    search_fields = ['title'] # Пошук по тайтлу(Можна по любій моделі)
    list_per_page = 200  # Скільки елеметів буде відображатись на одній сторінці(дефаут 100)

admin.site.register(Post, PostModelAdmin)