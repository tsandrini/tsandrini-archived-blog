# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170820_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='active',
            field=models.BooleanField(default=True, help_text="Non active pages won't be shown", verbose_name='Aktivní'),
        ),
        migrations.AlterField(
            model_name='page',
            name='dynamic',
            field=models.BooleanField(default=False, help_text='Non-dynamic pages does not provide content from database storage, but have a static template instead', verbose_name='Dynamic'),
        ),
    ]
