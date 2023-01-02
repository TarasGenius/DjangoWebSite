from django.db import models


class Goods(models.Model):
    title = models.CharField(max_length=20, help_text='Enter name')
    price = models.IntegerField(default=0)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    description = models.TextField(help_text='Enter description')
    id = models.CharField(max_length=5, help_text='Enter product code', primary_key=True)

    def __str__(self):
        return self.title
