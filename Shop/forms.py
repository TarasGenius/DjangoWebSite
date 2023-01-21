from django import forms
from Shop.models import Goods


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = [
            'title',
            'description',
            'topic',
            'price'
        ]