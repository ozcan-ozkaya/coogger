# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-26 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooggerapp', '0003_auto_20170927_0141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-time'], 'verbose_name': 'İçerik'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user_topic',
        ),
    ]
