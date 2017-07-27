# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-26 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_in',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='departments',
            name='dept_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='interests',
            name='interest_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='bio',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='student',
            name='email_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=40),
        ),
    ]
