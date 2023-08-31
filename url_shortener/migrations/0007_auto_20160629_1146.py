# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 11:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0006_auto_20160629_0617'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='clicks_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='link',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2016, 6, 29, 11, 46, 20, 119212, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
