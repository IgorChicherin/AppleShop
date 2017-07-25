# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20170530_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='ipad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='iphone',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='iwatch',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='mac',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Категория'),
        ),
    ]