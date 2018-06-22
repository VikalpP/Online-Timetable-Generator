# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable_final1', '0004_auto_20180120_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='descipline_course_table',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='timetable_final1.descipline_course'),
        ),
        migrations.AddField(
            model_name='lab',
            name='descipline_course_table',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='timetable_final1.descipline_course'),
        ),
    ]
