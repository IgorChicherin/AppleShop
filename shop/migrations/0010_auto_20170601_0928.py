# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_goods_zindex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='zindex',
            field=models.BooleanField(default=0, verbose_name='Текст поверх картинки'),
        ),
    ]
