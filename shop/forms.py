from django import forms
from .models import Goods


class MacContent(forms.ModelForm):
    name = forms.CharField(label='Название')
    head = forms.CharField(label='Заголовок')
    img_lg = forms.ImageField(label='Картинка большая')
    img_md = forms.ImageField(label='Картинка средняя', required=False)
    img_sm = forms.ImageField(label='Картинка маленькая')

    class Meta:
        model = Goods
        fields = '__all__'
