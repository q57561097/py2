# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='网址')),
                ('content', models.TextField(blank=True, verbose_name='内容', default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '教程',
                'verbose_name': '教程',
            },
        ),
        migrations.AlterModelOptions(
            name='biaoti',
            options={'ordering': ['name'], 'verbose_name_plural': '栏目2', 'verbose_name': '栏目1'},
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='news.biaoti', verbose_name='归属栏目'),
        ),
    ]
