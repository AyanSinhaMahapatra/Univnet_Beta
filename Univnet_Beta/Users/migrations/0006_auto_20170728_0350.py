# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20170728_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni',
            old_name='cv_url',
            new_name='cv',
        ),
        migrations.RenameField(
            model_name='alumni',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='cv_url',
            new_name='cv',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='image_url',
            new_name='image',
        ),
    ]
