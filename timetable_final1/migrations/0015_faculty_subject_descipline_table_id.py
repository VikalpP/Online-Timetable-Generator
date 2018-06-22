# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-25 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable_final1', '0014_temp_lab_descipline_course_table_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_subject',
            name='descipline_table_id',
            field=models.ForeignKey(db_column=b'descipline_table_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='timetable_final1.descipline_course'),
        ),
    ]