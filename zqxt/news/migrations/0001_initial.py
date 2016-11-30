# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biaoti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='栏目名称', max_length=256)),
                ('slug', models.CharField(verbose_name='栏目网址', max_length=256, db_index=True)),
                ('intro', models.TextField(default='', verbose_name='栏目简介')),
            ],
        ),
    ]
