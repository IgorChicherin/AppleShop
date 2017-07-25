from django.db import models


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=50)
    head = models.CharField(max_length=50)
    text = models.TextField(max_length=100, blank=True, verbose_name='Текст')
    img_lg = models.ImageField()
    img_md = models.ImageField(blank=True)
    img_sm = models.ImageField(blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория')
    zindex = models.BooleanField(default=0, verbose_name='Текст поверх картинки')

class Category(models.Model):
    name = models.CharField(unique=False, max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name
