# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
