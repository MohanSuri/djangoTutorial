# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=100)),
                ('level', models.CharField(choices=[('EASY', 'easy'), ('MEDIUM', 'medium'), ('HARD', 'hard')], default='EASY', max_length=100)),
                ('solution', models.CharField(default='', max_length=5)),
            ],
        ),
    ]
