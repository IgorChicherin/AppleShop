# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20170531_1422'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Iphone',
            new_name='Goods',
        ),
        migrations.RemoveField(
            model_name='ipad',
            name='category',
        ),
        migrations.RemoveField(
            model_name='iwatch',
            name='category',
        ),
        migrations.RemoveField(
            model_name='mac',
            name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
        migrations.DeleteModel(
            name='Ipad',
        ),
        migrations.DeleteModel(
            name='Iwatch',
        ),
        migrations.DeleteModel(
            name='Mac',
        ),
    ]
