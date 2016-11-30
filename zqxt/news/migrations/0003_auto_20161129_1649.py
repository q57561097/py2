# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20161129_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 29, 8, 49, 27, 705289, tzinfo=utc), verbose_name='发表时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='更新时间'),
        ),
    ]
