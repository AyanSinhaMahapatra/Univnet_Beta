# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20170728_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
