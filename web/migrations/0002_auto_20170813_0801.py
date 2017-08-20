# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='dynamic',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
