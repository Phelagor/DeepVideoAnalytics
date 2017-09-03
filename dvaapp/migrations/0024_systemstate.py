# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0023_auto_20170902_0516'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('tasks', models.IntegerField(default=0)),
                ('pending_tasks', models.IntegerField(default=0)),
                ('completed_tasks', models.IntegerField(default=0)),
                ('processes', models.IntegerField(default=0)),
                ('pending_processes', models.IntegerField(default=0)),
                ('completed_processes', models.IntegerField(default=0)),
            ],
        ),
    ]
