from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    update = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0) # Поле для вводу цілих чисел
    slug = models.SlugField() # Поле для вводу ексту(макс 50 літер) тільки літери, цифри, подкреслення та дефіси


    def __str__(self):
        return self.title