# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.

License for BK-ITSM 蓝鲸流程服务:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Generated by Django 1.11.24 on 2020-05-01 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_sopstask_bk_biz_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='创建人')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('updated_by', models.CharField(max_length=64, verbose_name='修改人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否软删除')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('name', models.CharField(max_length=255, verbose_name='任务库')),
                ('tasks', jsonfield.fields.JSONField(default=[], max_length=10000, verbose_name='任务列表')),
            ],
            options={'verbose_name': '任务库', 'verbose_name_plural': '任务库', 'ordering': ('-id',),},
            managers=[('_objects', django.db.models.manager.Manager()),],
        ),
    ]