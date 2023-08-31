# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 18:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_auto_20160621_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='click_count',
        ),
        migrations.AlterField(
            model_name='link',
            name='alias',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Alias can only contain alphabets, numerals, underscores and hyphens', regex='^[a-zA-Z0-9-_]+$')]),
        ),
    ]
