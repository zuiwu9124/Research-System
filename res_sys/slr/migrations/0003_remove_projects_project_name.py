# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slr', '0002_auto_20160329_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='project_name',
        ),
    ]
