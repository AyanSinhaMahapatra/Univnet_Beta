# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0018_auto_20170729_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='school_studied',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Users.School'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumni',
            name='univ_studyied',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='alumni_requests_created', to='Users.University'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumni',
            name='work',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Users.University'),
            preserve_default=False,
        ),
    ]
