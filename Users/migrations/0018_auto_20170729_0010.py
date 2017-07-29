# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0017_auto_20170729_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='dept_alum',
        ),
        migrations.AddField(
            model_name='alumni',
            name='experience',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumni',
            name='projects_info',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumni',
            name='publications',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]