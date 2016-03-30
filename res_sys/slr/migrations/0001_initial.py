# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.IntegerField()),
                ('user_authority', models.IntegerField()),
                ('other_request', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('project_info', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('authority', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cellphone', models.CharField(blank=True, max_length=100)),
                ('sex', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slr.Users'),
        ),
    ]