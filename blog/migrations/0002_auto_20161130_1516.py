# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 15:16
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='\u5185\u5bb9'),
        ),
    ]
