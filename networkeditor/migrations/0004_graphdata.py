# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkeditor', '0003_networkconnection'),
    ]

    operations = [
        migrations.CreateModel(
            name='graphdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphname', models.TextField()),
                ('graphid', models.TextField()),
                ('datestamp', models.DateField(auto_now_add=True)),
                ('timestamp', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
