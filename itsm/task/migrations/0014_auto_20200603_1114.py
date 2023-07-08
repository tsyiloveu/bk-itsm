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

# Generated by Django 1.11.24 on 2020-06-03 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_remove_tasklib_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(
                choices=[
                    ('NEW', '新建'),
                    ('QUEUE', '待处理'),
                    ('WAITING_FOR_OPERATE', '待处理'),
                    ('WAITING_FOR_BACKEND', '后台处理中'),
                    ('RUNNING', '执行中'),
                    ('WAITING_FOR_CONFIRM', '待总结'),
                    ('SKIPPED', '已忽略'),
                    ('FAILED', '失败'),
                    ('FINISHED', '完成'),
                ],
                default='NEW',
                max_length=64,
                verbose_name='任务的状态',
            ),
        ),
        migrations.AlterField(
            model_name='taskfield',
            name='type',
            field=models.CharField(
                choices=[
                    ('STRING', '单行文本'),
                    ('TEXT', '多行文本'),
                    ('INT', '数字'),
                    ('DATE', '日期'),
                    ('DATETIME', '时间'),
                    ('DATETIMERANGE', '时间间隔'),
                    ('TABLE', '表格'),
                    ('SELECT', '单选下拉框'),
                    ('INPUTSELECT', '可输入单选下拉框'),
                    ('MULTISELECT', '多选下拉框'),
                    ('CHECKBOX', '复选框'),
                    ('RADIO', '单选框'),
                    ('MEMBER', '单选人员选择'),
                    ('MEMBERS', '多选人员选择'),
                    ('RICHTEXT', '富文本'),
                    ('FILE', '附件上传'),
                    ('CUSTOMTABLE', '自定义表格'),
                    ('TREESELECT', '树形选择'),
                    ('LINK', '链接'),
                    ('CASCADE', '级联'),
                ],
                default='STRING',
                max_length=32,
                verbose_name='字段类型',
            ),
        ),
    ]