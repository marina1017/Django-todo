# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-30 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_todo_bord_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_bord',
            name='image_url',
        ),
    ]
