# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170809_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
