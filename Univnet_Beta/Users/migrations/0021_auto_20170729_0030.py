# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 19:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0020_alumni_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni',
            old_name='univ_studyied',
            new_name='univ_studied',
        ),
    ]
