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

# Generated by Django 1.11.11 on 2019-09-19 15:20


import django.db.models.deletion
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                (
                    'action_type',
                    models.CharField(
                        choices=[
                            ('alert', '\u544a\u8b66\u4e8b\u4ef6'),
                            ('color_set', '\u989c\u8272\u4e8b\u4ef6'),
                            ('ticket_set', '\u5355\u636e\u66f4\u65b0\u4e8b\u4ef6'),
                        ],
                        max_length=32,
                        verbose_name='\u4e8b\u4ef6\u7c7b\u578b',
                    ),
                ),
                (
                    'config',
                    jsonfield.fields.JSONField(
                        default={},
                        help_text='\u7c7b\u578b\u8be6\u7ec6\u914d\u7f6e',
                        verbose_name='\u4e8b\u4ef6\u914d\u7f6e',
                    ),
                ),
            ],
            options={
                'verbose_name': '\u5347\u7ea7\u4e8b\u4ef6\u914d\u7f6e',
                'verbose_name_plural': '\u5347\u7ea7\u4e8b\u4ef6\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='ActionPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('name', models.CharField(max_length=255, verbose_name='\u7b56\u7565\u540d\u79f0')),
                ('order', models.IntegerField(default=-1, verbose_name='\u7b56\u7565\u987a\u5e8f')),
                (
                    'condition',
                    jsonfield.fields.JSONField(
                        help_text='\u5f53\u8fbe\u5230\u6761\u4ef6\u7684\u65f6\u5019\uff0c\u53ef\u4ee5\u89e6\u53d1\u4e0d\u540c\u7684\u52a8\u4f5c',
                        verbose_name='\u5347\u7ea7\u6761\u4ef6',
                    ),
                ),
                ('actions', models.ManyToManyField(help_text='\u5904\u7406\u4e8b\u4ef6', to='sla.Action')),
            ],
            options={'verbose_name': '\u5347\u7ea7\u7b56\u7565', 'verbose_name_plural': '\u5347\u7ea7\u7b56\u7565',},
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('name', models.CharField(max_length=255, verbose_name='\u5047\u671f\u540d\u79f0')),
                (
                    'day_of_week',
                    models.CharField(
                        choices=[
                            (0, 'MONDAY'),
                            (1, 'TUESDAY'),
                            (2, 'WEDNESDAY'),
                            (3, 'THURSDAY'),
                            (4, 'FRIDAY'),
                            (5, 'SATURDAY'),
                            (6, 'SUNDAY'),
                        ],
                        default=-1,
                        max_length=32,
                        verbose_name='\u661f\u671f\u51e0',
                    ),
                ),
                (
                    'type_of_day',
                    models.CharField(
                        choices=[
                            ('NORMAL', '\u5e38\u89c4\u65e5'),
                            ('WORKDAY', '\u52a0\u73ed\u65e5'),
                            ('HOLIDAY', '\u8282\u5047\u65e5'),
                        ],
                        default='NORMAL',
                        max_length=32,
                        verbose_name='\u65e5\u671f\u7c7b\u578b',
                    ),
                ),
                ('start_date', models.DateField(null=True, verbose_name='\u5f00\u59cb\u65e5\u671f')),
                ('end_date', models.DateField(null=True, verbose_name='\u7ed3\u675f\u65e5\u671f')),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u65e5\u548c\u8282\u5047\u65e5',
                'verbose_name_plural': '\u5de5\u4f5c\u65e5\u548c\u8282\u5047\u65e5',
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('name', models.CharField(max_length=255, verbose_name='\u65f6\u95f4\u6bb5\u540d\u79f0')),
                ('start_time', models.TimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.TimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5de5\u4f5c\u65f6\u95f4\u6bb5',
                'verbose_name_plural': '\u5de5\u4f5c\u65f6\u95f4\u6bb5',
            },
        ),
        migrations.CreateModel(
            name='PriorityMatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('service_type', models.CharField(max_length=64, verbose_name='\u670d\u52a1\u7c7b\u578b')),
                ('urgency', models.CharField(max_length=255, verbose_name='\u7d27\u6025\u7a0b\u5ea6')),
                ('impact', models.CharField(max_length=255, verbose_name='\u5f71\u54cd\u8303\u56f4')),
                ('priority', models.CharField(max_length=255, verbose_name='\u4f18\u5148\u7ea7')),
            ],
            options={
                'verbose_name': '\u4f18\u5148\u7ea7\u77e9\u9635',
                'verbose_name_plural': '\u4f18\u5148\u7ea7\u77e9\u9635',
            },
        ),
        migrations.CreateModel(
            name='PriorityPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('name', models.CharField(max_length=255, verbose_name='\u7b56\u7565\u540d\u79f0')),
                ('priority', models.CharField(max_length=255, verbose_name='\u4f18\u5148\u7ea7')),
                ('handle_time', models.IntegerField(default=0, verbose_name='\u5904\u7406\u671f\u9650')),
                (
                    'handle_unit',
                    models.CharField(
                        choices=[('m', '\u5206\u949f'), ('h', '\u5c0f\u65f6'), ('d', '\u5929')],
                        default='m',
                        max_length=32,
                        verbose_name='\u65f6\u957f\u5355\u4f4d',
                    ),
                ),
            ],
            options={'verbose_name': '\u670d\u52a1\u7b56\u7565', 'verbose_name_plural': '\u670d\u52a1\u7b56\u7565',},
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                (
                    'is_enabled',
                    models.BooleanField(
                        default=True,
                        help_text='\u662f\uff1a\u542f\u7528\u5f53\u524d\u5de5\u4f5c\u65e5\u5386\u914d\u7f6e\uff0c \u5426\uff1a\u9ed8\u8ba4\u91c7\u75287*24\u5c0f\u65f6',
                        verbose_name='\u914d\u7f6e\u662f\u5426\u751f\u6548',
                    ),
                ),
                (
                    'days',
                    models.ManyToManyField(help_text='\u5e38\u89c4\u65e5\u5386', related_name='days', to='sla.Day'),
                ),
                (
                    'holidays',
                    models.ManyToManyField(
                        default=None, help_text='\u5047\u671f', related_name='holidays', to='sla.Day'
                    ),
                ),
                (
                    'workdays',
                    models.ManyToManyField(
                        default=None, help_text='\u52a0\u73ed\u65e5', related_name='workdays', to='sla.Day'
                    ),
                ),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u8fd0\u8425\u65f6\u95f4',
                'verbose_name_plural': '\u670d\u52a1\u8fd0\u8425\u65f6\u95f4',
            },
        ),
        migrations.CreateModel(
            name='Sla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('name', models.CharField(max_length=255, verbose_name='Sla\u540d\u79f0')),
                ('is_enabled', models.BooleanField(default=False, verbose_name='\u662f\u5426\u542f\u7528')),
                (
                    'action_policies',
                    models.ManyToManyField(
                        help_text='\u670d\u52a1\u5347\u7ea7\u4e8b\u4ef6\u7b56\u7565',
                        related_name='a_slas',
                        to='sla.ActionPolicy',
                    ),
                ),
                (
                    'policies',
                    models.ManyToManyField(
                        help_text='\u670d\u52a1\u4f18\u5148\u7ea7\u7b56\u7565',
                        related_name='p_slas',
                        to='sla.PriorityPolicy',
                    ),
                ),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u4f18\u5148\u7ea7',
                'verbose_name_plural': '\u670d\u52a1\u4f18\u5148\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='SlaTimerRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64, verbose_name='\u521b\u5efa\u4eba')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updated_by', models.CharField(max_length=64, verbose_name='\u4fee\u6539\u4eba')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8f6f\u5220\u9664')),
                ('service_type', models.CharField(max_length=64, verbose_name='\u670d\u52a1\u7c7b\u578b')),
                ('name', models.CharField(default='', max_length=255, verbose_name='\u89c4\u5219\u540d\u79f0')),
                (
                    'condition_type',
                    models.CharField(
                        choices=[('START', '\u5f00\u59cb'), ('END', '\u7ed3\u675f'), ('PAUSE', '\u6682\u505c')],
                        default='START',
                        max_length=64,
                        verbose_name='\u6761\u4ef6\u7c7b\u578b',
                    ),
                ),
                ('condition', jsonfield.fields.JSONField(default={}, verbose_name='\u6761\u4ef6')),
            ],
            options={'verbose_name': '\u8ba1\u65f6\u89c4\u5219', 'verbose_name_plural': '\u8ba1\u65f6\u89c4\u5219',},
        ),
        migrations.AddField(
            model_name='prioritypolicy',
            name='schedule',
            field=models.ForeignKey(
                help_text='\u670d\u52a1\u65f6\u95f4',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='policies',
                to='sla.Schedule',
            ),
        ),
        migrations.AlterUniqueTogether(name='prioritymatrix', unique_together={('service_type', 'urgency', 'impact')},),
        migrations.AddField(
            model_name='day',
            name='duration',
            field=models.ManyToManyField(
                help_text='\u5de5\u4f5c\u65f6\u95f4\u6bb5\uff0c\u6ca1\u6709\u914d\u7f6e\u7684\u60c5\u51b5\u4e0b\uff0c\u9ed8\u8ba4\u4ece0:00 -23:59',
                to='sla.Duration',
            ),
        ),
    ]
