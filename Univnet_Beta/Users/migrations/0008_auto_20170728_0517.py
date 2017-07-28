# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20170728_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='student',
            name='cv',
        ),
        migrations.AddField(
            model_name='alumni',
            name='cv_url',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='student',
            name='cv_url',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
