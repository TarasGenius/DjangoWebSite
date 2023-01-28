from django.db import models


class Goods(models.Model):
    choices_list = [
        ('laptop', 'laptop'),
        ('desktop', 'desktop'),


    ]
    title = models.CharField(max_length=20, help_text='Enter name')
    price = models.IntegerField(default=0)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    description = models.TextField(help_text='Enter description')
    topic = models.TextField(choices=choices_list)

    def get_absolut_url(self):

        return f'/shop/detail/{self.id}'

    def get_list_topic(self):
        lst = []
        for i in self.choices_list:
            lst.append(i[0])
        return lst

    def __str__(self):
        return self.title
