# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 09:45
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkeditor', '0004_graphdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkconnection',
            name='ConnectedPoints',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), size=None),
        ),
        migrations.AlterField(
            model_name='networkconnection',
            name='networkid',
            field=models.TextField(),
        ),
    ]
