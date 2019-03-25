# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-17 05:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190317_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 17, 5, 21, 2, 781023, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 17, 5, 21, 2, 780317, tzinfo=utc)),
        ),
    ]
